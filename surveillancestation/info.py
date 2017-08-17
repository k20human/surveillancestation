import os
import time
from .api import Api


class Info:
    def __init__(self, api: Api):
        self._api = api
        self._cgi_path = 'entry.cgi'
        self._api_name = 'SYNO.SurveillanceStation.Info'
        self._version = api.get_max_version(self._api_name)

    """Get Surveillance Station information"""

    def get_info(self):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='GetInfo'))
