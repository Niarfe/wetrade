import time
import requests
from pyotp import TOTP
from contextlib import suppress
from playwright.sync_api import sync_playwright
from authlib.integrations.requests_client import OAuth1Session
from wetrade.utils import log_in_background, parse_response_data
try: 
  import settings
except ModuleNotFoundError:
  import wetrade.project_template.settings as settings


class Connection:
    def __init__(self, settings):
        self.config = settings.config
        self.client = OAuth1Session(
            client_id = self.config['client_key'], 
            client_secret = self.config['client_secret'],
            redirect_uri = 'oob'
            )
        self.authorize_url = None
        self.text_code = None

    def set_text_code(self, authorize_url):

        print('login_url', authorize_url)
        self.text_code = input('Login through url and enter code: ')
        return self.text_code
    
    
    def set_authorize_url(self, config={}):

        request_token = self.client.fetch_request_token(
            url = 'https://api.etrade.com/oauth/request_token',
            params = {'format': 'json'}
            )

        key =  self.config['client_key']
        token = request_token['oauth_token']

        self.authorize_url = f"https://us.etrade.com/e/t/etws/authorize?key={key}&token={token}"
        return self.authorize_url
    
    def new_session(self, authorize_url=None, text_code=None):
        set_authorize_url(self.config)
    
        set_text_code(authorize_url)
   
        try:
            self.client.fetch_access_token(
                url = 'https://api.etrade.com/oauth/access_token',
                verifier = self.text_code
                )
            return self.client
        except Exception as e: # text code is blank or incorrect
            log_in_background(
                called_from = 'new_session',
                tags = ['user-message'], 
                message = f"{time.strftime('%H:%M:%S', time.localtime())} : Error getting access token, retrying login",
                e = e
                )
            return new_session(self.config)
  
class UserSession:
  def __init__(self, config={}):
    self.config = settings.config if config == {} else config
    self.session = new_session(self.config)
    self.logged_in = True

  def renew_token(self):
    self.logged_in = False
    r = self.session.get(url='https://api.etrade.com/oauth/renew_access_token')
    if r.status_code != 200:
      self.logged_in = True
    else:
      log_in_background(
        called_from = 'renew_token',
        tags = ['user-message'], 
        message = time.strftime('%H:%M:%S', time.localtime()) + ': Error renewing access token')
      self.login()

  def login(self):
    self.logged_in = False
    try:
      self.session = new_session(self.config)
      self.logged_in = True
    except Exception as e:
      log_in_background(
        called_from = 'login',
        tags = ['user-message'], 
        message = time.strftime('%H:%M:%S', time.localtime()) + ': Error, retrying login',
        e = e)
      self.login()

  def post(self, *args, **kwargs):
    return self.handle_request('POST', args, kwargs)
      
  def get(self, *args, **kwargs):
    return self.handle_request('GET', args, kwargs)

  def put(self, *args, **kwargs):
    return self.handle_request('PUT', args, kwargs)
  
  def handle_request(self, http_method, args, kwargs):
    if self.logged_in:
      url = kwargs['url'] if 'url' in kwargs else ''
      try:
        r = self.session.request(http_method, *args, **kwargs, timeout=30)
      except Exception as e:
        error_num = 0
        error_msg = ''
        with suppress(Exception):
          error_num = e.args[0].args[1].errno
          error_msg = e.args[0].reason.message
        if isinstance(e, requests.exceptions.ConnectionError):
          if error_num == 104:
            log_in_background(
              called_from = 'UserSession.handle_request', 
              tags = ['user-message', 'connection-error', 'connection-reset'], 
              message = time.strftime('%H:%M:%S', time.localtime()) + ': Connection reset, retrying request',
              url = url,
              e = e)
            return self.handle_request(http_method, args, kwargs)
          else:
            log_in_background(
              called_from = 'UserSession.handle_request', 
              tags = ['user-message', 'connection-error'], 
              message = time.strftime('%H:%M:%S', time.localtime()) + ': Connection error ({}), retrying request'.format(str(error_msg)), 
              url = url,
              e = e)
            return self.handle_request(http_method, args, kwargs)
        elif isinstance(e, requests.exceptions.Timeout):
          log_in_background(
            called_from = 'UserSession.handle_request', 
            tags = ['user-message', 'connection-timeout'], 
            message = time.strftime('%H:%M:%S', time.localtime()) + ': Request timed out, retrying request',
            url = url,
            e = e)
          return self.handle_request(http_method, args, kwargs)
        else:
          log_in_background(
            called_from = 'UserSession.handle_request',
            tags = ['user-message', 'connection-unknown'], 
            message = time.strftime('%H:%M:%S', time.localtime()) + ': User session disconnected, reconnecting',
            url = url,
            e = e) 
          self.login()
          return self.handle_request(http_method, args, kwargs)
      if r.status_code == 500:
        log_in_background(
          called_from = 'UserSession.handle_request',
          tags = ['user-message', 'internal-server-error'],
          message = time.strftime('%H:%M:%S', time.localtime()) + ': Internal Server Error, waiting 1 second then retrying request',
          url = url,
          r = r)
        time.sleep(1)
        return self.handle_request(http_method, args, kwargs)
      content = parse_response_data(r)
      if 'Error' in content:
        if not isinstance(content, str):
          if 'code' in content['Error'] and content['Error']['code'] == 100: # retry if service unavailable
            log_in_background(
              called_from = 'UserSession.handle_request',
              tags = ['user-message', 'endpoint-unavailable'], 
              message = time.strftime('%H:%M:%S', time.localtime()) + ': Endpoint unavailable, retrying request',
              url = url,
              r = r)
            return self.handle_request(http_method, args, kwargs)
          elif 'message' in content['Error'] and content['Error']['message'] == 'oauth_problem=token_rejected':
            log_in_background(
              called_from = 'UserSession.handle_request',
              tags = ['user-message', 'token-rejected'], 
              message = time.strftime('%H:%M:%S', time.localtime()) + ': Rejected user token, reconnecting',
              url = url,
              r = r)
            self.login()
            return self.handle_request(http_method, args, kwargs)
        else: # non-json response with "Error"
          log_in_background(
            called_from = 'UserSession.handle_request',
            tags = ['user-message', 'server-error-unknown'], 
            message = time.strftime('%H:%M:%S', time.localtime()) + ': Unknown error, retrying request',
            url = url,
            r = r)
          return self.handle_request(http_method, args, kwargs)
      return r
    else:
      log_in_background(
        called_from = 'UserSession.handle_request',
        message = time.strftime('%H:%M:%S', time.localtime()) + ': Waiting for login',
        tags = ['user-message'])
      time.sleep(3)
      return self.handle_request(http_method, args, kwargs)

class SimpleUserSession(UserSession):
  def handle_request(self, http_method, args, kwargs):
    return self.session.request(http_method, *args, **kwargs, timeout=30)
