import os
import time
from .api import Api


class NotificationSchedule:
    def __init__(self, api: Api):
        self._api = api
        self._cgi_path = 'entry.cgi'
        self._api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        self._version = api.get_max_version(self._api_name)

    """Get schedule of system dependent events"""

    def get_system_dependent_schedule(self, event_group_types=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='GetSystemDependentSchedule',
                                                                extra={
                                                                    'eventGroupTypes': event_group_types
                                                                }))

    """Batch set schedule. Group id, camera id are required if needed"""

    def set_batch_schedule(self, event_types=(), schedule=(), camera_ids=(), camera_group_ids=(), filter=0):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='SetBatchSchedule',
                                                                extra={
                                                                    'eventTypes': ",".join(event_types),
                                                                    'schedule': schedule,
                                                                    'cameraIds': ",".join(camera_ids),
                                                                    'cameraGroupIds': ",".join(camera_group_ids),
                                                                    'filter': filter
                                                                }))

    """Get schedule of camera"""

    def get_camera_schedule(self, camera_id=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='GetCameraSchedule',
                                                                extra={
                                                                    'cameraId': camera_id
                                                                }))

    """Set schedule of camera"""

    def set_camera_schedule(self, event_type=0, schedule=(), camera_id=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='SetCameraSchedule',
                                                                extra={
                                                                    'eventType': event_type,
                                                                    'schedule': schedule,
                                                                    'cameraId': camera_id
                                                                }))


class Notification:
    def __init__(self, api: Api):
        self._api = api
        self._cgi_path = 'entry.cgi'
        self._api_name = 'SYNO.SurveillanceStation.Notification'
        self._version = api.get_max_version(self._api_name)

        # Sub API
        self._sub_api_schedule = NotificationSchedule(self._api)

    @property
    def schedule(self) -> NotificationSchedule:
        return self._sub_api_schedule

