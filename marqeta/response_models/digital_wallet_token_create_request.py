from datetime import datetime
from marqeta.response_models.digital_wallet_token_card_info import DigitalWalletTokenCardInfo
from marqeta.response_models.digital_wallet_token import DigitalWalletToken
from marqeta.response_models.digital_wallet_token_device import DigitalWalletTokenDevice
from marqeta.response_models.digital_wallet_token_wallet_provider import DigitalWalletTokenWalletProvider
from marqeta.response_models.digital_wallet_token_request_address import DigitalWalletTokenRequestAddress

class DigitalWalletTokenCreateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

    @property
    def digital_wallet_token_card_info(self):
        if 'digital_wallet_token_card_info' in self.json_response:
            return DigitalWalletTokenCardInfo(self.json_response['digital_wallet_token_card_info'])

    @property
    def digital_wallet_token(self):
        if 'digital_wallet_token' in self.json_response:
            return DigitalWalletToken(self.json_response['digital_wallet_token'])

    @property
    def digital_wallet_token_device(self):
        if 'digital_wallet_token_device' in self.json_response:
            return DigitalWalletTokenDevice(self.json_response['digital_wallet_token_device'])

    @property
    def digital_wallet_token_wallet_provider(self):
        if 'digital_wallet_token_wallet_provider' in self.json_response:
            return DigitalWalletTokenWalletProvider(self.json_response['digital_wallet_token_wallet_provider'])

    @property
    def digital_wallet_token_request_address(self):
        if 'digital_wallet_token_request_address' in self.json_response:
            return DigitalWalletTokenRequestAddress(self.json_response['digital_wallet_token_request_address'])
