preview_order_response = {
  'PreviewOrderResponse': {
    'Disclosure': {
      'aoDisclosureFlag': False,
      'conditionalDisclosureFlag': True,
      'ehDisclosureFlag': False},
    'MessageList': {},
    'Order': [{
      'Instrument': [{
        'Product': {
          'securityType': 'EQ',
          'symbol': 'IBM'},
        'cancelQuantity': 0,
        'orderAction': 'BUY',
        'quantity': 100,
        'quantityType': 'QUANTITY',
        'reserveOrder': False,
        'reserveQuantity': 0,
        'symbolDescription': ''}],
      'allOrNone': False,
      'egQual': 'EG_QUAL_OUTSIDE_GUARANTEED_PERIOD',
      'estimatedCommission': 6.99,
      'estimatedFees': 0.0,
      'gcd': 0,
      'limitPrice': 120,
      'marketSession': 'EXTENDED',
      'messages': {},
      'netAsk': 0,
      'netBid': 0,
      'netPrice': 0,
      'orderTerm': 'GOOD_FOR_DAY',
      'priceType': 'LIMIT',
      'ratio': '',
      'stopPrice': 0}],
    'PortfolioMargin': {
      'houseExcessEquityChange': 0.0,
      'houseExcessEquityCurr': 0.0,
      'houseExcessEquityNew': 0.0,
      'pmEligible': False},
    'PreviewIds': [{'previewId': 1627181131}],
    'accountId': '835376230',
    'dstFlag': False,
    'marginLevelCd': 'MARGIN_TRADING_ALLOWED',
    'optionLevelCd': 4,
    'orderType': 'EQ',
    'previewTime': 1354512315217}}

place_order_response = {
  'PlaceOrderResponse': {
    'MessageList': {},
    'Order': [{
      'Instrument': [{
        'Product': {
          'securityType': 'EQ',
          'symbol': 'IBM'},
        'cancelQuantity': 0,
        'orderAction': 'BUY',
        'quantity': 100,
        'quantityType': 'QUANTITY',
        'reserveOrder': False,
        'reserveQuantity': 0,
        'symbolDescription': ''}],
      'allOrNone': False,
      'egQual': 'EG_QUAL_QUALIFIED',
      'estimatedCommission': 7.99,
      'estimatedFees': 0.0,
      'gcd': 0,
      'limitPrice': 120,
      'marketSession': 'REGULAR',
      'messages': {
        'Message': [{
          'code': 1026,
          'description': 'Normal: '
          'order '
          'created',
          'type': 'WARNING'}]},
      'netAsk': 0,
      'netBid': 0,
      'netPrice': 0,
      'orderTerm': 'GOOD_UNTIL_CANCEL',
      'priceType': 'LIMIT',
      'ratio': '',
      'stopPrice': 0}],
    'OrderIds': [{'orderId': 529}],
    'PortfolioMargin': {
      'houseExcessEquityChange': 0.0,
      'houseExcessEquityCurr': 0.0,
      'houseExcessEquityNew': 0.0,
      'pmEligible': False},
    'accountId': '837108000',
    'dstFlag': False,
    'marginLevelCd': 'MARGIN_TRADING_ALLOWED',
    'optionLevelCd': 4,
    'orderType': 'EQ',
    'placedTime': 1354532494528}}

preview_update_response = {
  'PreviewOrderResponse': {
    'MessageList': {},
    'Order': [{
      'Instrument': [{
        'Product': {
          'securityType': 'EQ',
          'symbol': 'IBM'},
        'cancelQuantity': 0,
        'orderAction': 'SELL_SHORT',
        'quantity': 100,
        'quantityType': 'QUANTITY',
        'reserveOrder': False,
        'reserveQuantity': 0,
        'symbolDescription': ''}],
      'allOrNone': False,
      'egQual': 'EG_QUAL_OUTSIDE_GUARANTEED_PERIOD',
      'estimatedCommission': 6.99,
      'estimatedFees': 0.0,
      'gcd': 0,
      'limitPrice': 0,
      'marketSession': 'REGULAR',
      'messages': {},
      'netAsk': 0,
      'netBid': 0,
      'netPrice': 0,
      'orderTerm': 'GOOD_UNTIL_CANCEL',
      'priceType': 'STOP',
      'ratio': '',
      'stopPrice': 171}],
    'PortfolioMargin': {
      'houseExcessEquityChange': 0.0,
      'houseExcessEquityCurr': 0.0,
      'houseExcessEquityNew': 0.0,
      'pmEligible': False},
    'PreviewIds': [{'previewId': 1627181131}],
    'accountId': '83537623',
    'dstFlag': False,
    'marginLevelCd': 'MARGIN_TRADING_ALLOWED',
    'optionLevelCd': 4,
    'orderType': 'EQ',
    'previewTime': 1354512315217}}

place_update_response = {
  'PlaceOrderResponse': {
    'orderType': 'EQ',
    'dstFlag': False,
    'optionLevelCd': 4,
    'marginLevelCd': 'MARGIN_TRADING_ALLOWED',
    'placedTime': 1354532494528,
    'accountId': '837108000',
    'MessageList': {},
    'Order': [{
      'orderTerm': 'GOOD_UNTIL_CANCEL',
      'priceType': 'LIMIT',
      'limitPrice': 171,
      'stopPrice': 0,
      'marketSession': 'REGULAR',
      'allOrNone': False,
      'messages': {
        'Message': [{
          'description': 'Normal: order created',
          'code': 1026,
          'type': 'WARNING'}]},
      'egQual': 'EG_QUAL_QUALIFIED',
      'estimatedCommission': 7.99,
      'estimatedFees': 0.0,
      'netPrice': 0,
      'netBid': 0,
      'netAsk': 0,
      'gcd': 0,
      'ratio': '',
      'Instrument': [{
        'symbolDescription': '',
        'orderAction': 'BUY',
        'quantityType': 'QUANTITY',
        'quantity': 100,
        'cancelQuantity': 0,
        'reserveOrder': False,
        'reserveQuantity': 0,
        'Product': {
          'symbol': 'IBM',
          'securityType': 'EQ'}}]}],
    'OrderIds': [{
      'orderId': 529}],
    'PortfolioMargin': {
      'houseExcessEquityNew': 0.0,
      'pmEligible': False,
      'houseExcessEquityCurr': 0.0,
      'houseExcessEquityChange': 0.0}}}

cancel_order_response = {
  'CancelOrderResponse': {
    'accountId': '837108000',
    'orderId': 529,
    'cancelTime': 0,
    'Messages': {
      'Message': [{
        'description': '200|Your request to cancel your order is being processed.',
        'code': 5011,
        'type': 'WARNING'}]}}}

order_status_response = {
  'OrdersResponse': {
    'Order': [{
      'orderId': 529,
      'orderType': 'EQ',
      'OrderDetail': [{
        'placedTime': 1354532494528,
        'orderValue': 120,
        'status': 'OPEN',
        'orderTerm': 'GOOD_FOR_DAY',
        'priceType': 'LIMIT',
        'limitPrice': 120,
        'stopPrice': 0,
        'marketSession': 'REGULAR',
        'replacesOrderId': 528,
        'allOrNone': False,
        'netPrice': 0,
        'netBid': 0,
        'netAsk': 0,
        'gcd': 0,
        'ratio': '',
        'Instrument': [{
          'symbolDescription': '',
          'orderAction': 'BUY',
          'quantityType': 'QUANTITY',
          'quantity': 100,
          'cancelQuantity': 0,
          'reserveOrder': False,
          'reserveQuantity': 0,
          'Product': {
            'symbol': 'IBM',
            'securityType': 'EQ'}}]}],
      'Events': {
        'Event': [{
          'name': 'ORDER_PLACED',
          'dateTime': 1354532494528,
          'Instrument': [{
            'symbolDescription': '',
            'orderAction': 'BUY',
            'quantityType': 'QUANTITY',
            'orderedQuantity': 100,
            'filledQuantity': 0.0,
            'estimatedCommission': 0.0,
            'estimatedFees': 0.0,
            'Product': {
              'symbol': 'IBM',
              'securityType': 'EQ'}}]}]}}]}} 