import os
import time

from .api import Api


class Info:
    def __init__(self, api: Api):
        self.api = api
        self.cgi_path = 'entry.cgi'
        self.api_name = 'SYNO.SurveillanceStation.Info'
        self.version = api.get_max_version(self.api_name)

    """Provide Surveillance Station information"""

    def get_info(self):
        return self.api.req(self.api_name, self.api.endpoint(api=self.api_name,
                                              cgi=self.cgi_path,
                                              version=self.version,
                                              method='GetInfo'))
