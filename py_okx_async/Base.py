import base64
import hmac
import json
from datetime import datetime
from typing import Optional, Union, Dict, Any
from urllib.parse import urlencode

from py_okx_async import exceptions
from py_okx_async.models import OKXCredentials, Methods
from py_okx_async.utils import async_get, async_post


class Base:
    """
    The base class for all section classes.

    Attributes:
        entrypoint_url: an entrypoint URL.

    """
    __credentials: OKXCredentials
    entrypoint_url: str

    def __init__(self, credentials: OKXCredentials, entrypoint_url: str) -> None:
        """
        Initialize the class.

        Args:
            credentials (OKXCredentials): an instance with all OKX API key data.
            entrypoint_url (str): an API entrypoint url.

        """
        self.__credentials = credentials
        self.entrypoint_url = entrypoint_url

    @staticmethod
    async def get_timestamp() -> str:
        """
        Get the current timestamp.

        Returns:
            str: the current timestamp.

        """
        return datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'

    async def generate_sign(self, timestamp: str, method: str, request_path: str, body: Union[dict, str]) -> bytes:
        """
        Generate signed message.

        Args:
            timestamp (str): the current timestamp.
            method (str): the request method is either GET or POST.
            request_path (str): the path of requesting an endpoint.
            body (Union[dict, str]): POST request parameters.

        Returns:
            bytes: the signed message.

        """
        if not body:
            body = ''

        if isinstance(body, dict):
            body = json.dumps(body)

        key = bytes(self.__credentials.secret_key, encoding='utf-8')
        msg = bytes(timestamp + method + request_path + body, encoding='utf-8')
        return base64.b64encode(hmac.new(key, msg, digestmod='sha256').digest())

    async def make_request(
            self, method: str, request_path: str, body: Optional[dict] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Make a request to the OKX API.

        Args:
            method (str): the request method is either GET or POST.
            request_path (str): the path of requesting an endpoint.
            body (Optional[dict]): request parameters. (None)

        Returns:
            Optional[Dict[str, Any]]: the request response.

        """
        timestamp = await self.get_timestamp()
        method = method.upper()
        body = body if body else {}
        if method == Methods.GET and body:
            request_path += f'?{urlencode(query=body)}'
            body = {}

        sign_msg = await self.generate_sign(timestamp=timestamp, method=method, request_path=request_path, body=body)
        url = self.entrypoint_url + request_path
        header = {
            'Content-Type': 'application/json',
            'OK-ACCESS-KEY': self.__credentials.api_key,
            'OK-ACCESS-SIGN': sign_msg.decode(),
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': self.__credentials.passphrase
        }
        if method == Methods.POST:
            response = await async_post(url, headers=header, data=json.dumps(body) if isinstance(body, dict) else body)

        else:
            response = await async_get(url, headers=header)

        if int(response.get('code')):
            raise exceptions.OKXAPIException(response=response)

        return response
