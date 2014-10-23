'''
    Author: Xyik
'''

from base import BaseCoinbaseAPI

#==============================================================================#

class CoinbaseAccountAPI(BaseCoinbaseAPI):

    def __init__(self, access_key, access_signature, access_nonce, version=None):
        super(CoinbaseAccountAPI, self).__init__(
                access_key, access_signature, access_nonce, version)

    # returns the user's current account balance in BTC.
    def account_balance(self, account_id=''):
        path = 'account/balance'
        path = 'account/%s/balance' % account_id if account_id else path
        return self.make_request(path, 'GET')

    # returns the user's current bitcoin receive address.
    def account_receieve_address(self):
        return self.make_request('account/receive_address', 'GET')

    # generates a new bitcoin receive address for the user.
    def account_generate_receieve_address(self):
        return self.make_request('account/generate_receive_address', 'POST')

    # returns all related changes to an account.
    def account_changes(self):
        return self.make_request('account_changes', 'GET')

    # returns the user's active accounts.
    def accounts(self, method='GET'):
        return self.make_request('accounts', method)

#==============================================================================#

class CoinbaseButtonAPI(BaseCoinbaseAPI):

    def __init__(self, access_key, access_signature, access_nonce, version=None):
        super(CoinbaseButtonAPI, self).__init__(
                access_key, access_signature, access_nonce, version)

    def buttons(self, name, button_type, subscription, price_string,
            price_currency_iso, callback_url, description, style,
            include_email=True):

        args = {
                'button' : {
                    'name' : name,
                    'price_string' : price_string,
                    'price_currency_iso' : price_currency_iso,
                    }
                }

        return self.make_request('buttons', 'POST', body_args=args)

#==============================================================================#

class CoinbaseAddressAPI(BaseCoinbaseAPI):

    def __init__(self, access_key, access_signature, access_nonce, version=None):
        super(CoinbaseAddressAPI, self).__init__(
                access_key, access_signature, access_nonce, version)

    def addresses(self):
        return self.make_request('addresses', 'GET')

#==============================================================================#

class CoinbaseCurrencyAPI(BaseCoinbaseAPI):

    def __init__(self, access_key, access_signature, access_nonce, version=None):
        super(CoinbaseCurrencyAPI, self).__init__(
                access_key, access_signature, access_nonce, version)

    def currencies(self):
        return self.make_request('currencies', 'GET')

    def currencies_exchange_rates(self):
        return self.make_request('currencies/exchange_rates', 'GET')

#==============================================================================#

class CoinbasePriceAPI(BaseCoinbaseAPI):

    def __init__(self, access_key, access_signature, access_nonce, version=None):
        super(CoinbasePriceAPI, self).__init__(
                access_key, access_signature, access_nonce, version)

    def prices_buy(self, qty=1):
        return self.make_request('prices/buy', 'GET', None, { 'qty' : qty } )

    def prices_sell(self):
        return self.make_request('prices/sell', 'GET')

    def prices_spot_rate(self):
        return self.make_request('prices/spot_rate', 'GET')

    def prices_historical(self):
        return self.make_request('prices/historical', 'GET')

#==============================================================================#

class CoinbaseAPI(BaseCoinbaseAPI):

    def __init__(self, access_key, access_signature, access_nonce, version=None):
        super(CoinbaseAPI, self).__init__(
                access_key, access_signature, access_nonce, version)

        self.account_api = CoinbaseAccountAPI(
                access_key, access_signature, access_nonce, version)
        self.button_api = CoinbaseButtonAPI(
                access_key, access_signature, access_nonce, version)
        self.price_api = CoinbasePriceAPI(
                access_key, access_signature, access_nonce, version)

#==============================================================================#
