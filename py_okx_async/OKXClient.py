import requests

from py_okx_async.Asset import Asset
from py_okx_async.models import OKXCredentials


class OKXClient:
    """
    The client that is used to interact with all functions.

    Attributes:
        entrypoint_url: an entrypoint URL.

    """
    __credentials: OKXCredentials
    entrypoint_url: str

    def __init__(self, credentials: OKXCredentials, entrypoint_url: str = 'https://www.okx.com') -> None:
        """
        Initialize the class.

        Args:
            credentials (OKXCredentials): an instance with all OKX API key data.
            entrypoint_url (str): an API entrypoint url. (https://www.okx.com)

        """
        self.__credentials = credentials
        self.entrypoint_url = entrypoint_url
        try:
            requests.get(self.entrypoint_url)

        except requests.exceptions.ConnectionError:
            self.entrypoint_url = 'https://www.okx.cab'
            requests.get(self.entrypoint_url)

        self.asset = Asset(credentials=self.__credentials, entrypoint_url=self.entrypoint_url)
