import requests
import time
import hmac
import hashlib

BASE_URL = "https://testnet.binance.vision"


class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _sign(self, params):
        query_string = "&".join([f"{k}={v}" for k, v in params.items() if v is not None])
        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def place_order(self, params):
        url = f"{BASE_URL}/api/v3/order"

        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {"X-MBX-APIKEY": self.api_key}

        response = requests.post(url, headers=headers, params=params)
        return response.json()