import os
import time
from .api import Api


class ActionRule:
    def __init__(self, api: Api):
        self._api = api
        self._cgi_path = 'entry.cgi'
        self._api_name = 'SYNO.SurveillanceStation.ActionRule'
        self._version = 1 # API version > 1 not document

    """List action rules"""

    def list(self, start=0, limit=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='List',
                                                                extra={
                                                                    'start': start,
                                                                    'limit': limit
                                                                }))

    """Disable action rules"""

    def disable(self, id_list=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='Disable',
                                                                extra={
                                                                    'idList': ",".join(id_list)
                                                                }))

    """Enable action rules"""

    def enable(self, id_list=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='Enable',
                                                                extra={
                                                                    'idList': ",".join(id_list)
                                                                }))

    """List all histories of action rule"""

    def list_history(self, start=0, limit=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='ListHistory',
                                                                extra={
                                                                    'start': start,
                                                                    'limit': limit
                                                                }))

    """Delete action rules"""

    def delete(self, id_list=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='Delete',
                                                                extra={
                                                                    'idList': ",".join(id_list)
                                                                }))

