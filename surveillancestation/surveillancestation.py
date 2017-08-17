import json
import logging

from .api import Api
from .info import Info
from .camera import Camera


class Surveillancestation:
    def __init__(self, host, user, passwd):
        self._api = Api(host=host, user=user, passwd=passwd)

        # API list
        self._api_info = None
        self._api_camera = None

    def logout(self):
        self._api.logout()

    @property
    def info(self):
        if self._api_info is None:
            self._api_info = Info(self._api)
        return self._api_info

    @property
    def camera(self):
        if self._api_camera is None:
            self._api_camera = Camera(self._api)
        return self._api_camera
