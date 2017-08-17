import os
import time
from .api import Api

class CameraGroup:
    def __init__(self, api: Api):
        self._api = api
        self._cgi_path = 'entry.cgi'
        self._api_name = 'SYNO.SurveillanceStation.Camera.Group'
        self._version = api.get_max_version(self._api_name)

class Camera:
    def __init__(self, api: Api):
        self._api = api
        self._cgi_path = 'entry.cgi'
        self._api_name = 'SYNO.SurveillanceStation.Camera'
        self._version = api.get_max_version(self._api_name)

        # Sub API
        self._sub_api_group = None

    @property
    def group(self):
        if self._sub_api_group is None:
            self._sub_api_group = CameraGroup(self._api)
        return self._sub_api_group

    """Get the list of all cameras"""

    def list(self, start=0, limit='', from_cam_list=False, include_deleted_cam=False, priv_cam_type=3, basic=False,
             stream_info=False, privilege=False, cam_stm=2):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='List',
                                                                extra={
                                                                    'start': start,
                                                                    'limit': limit,
                                                                    'blFromCamList': from_cam_list,
                                                                    'blIncludeDeletedCam': include_deleted_cam,
                                                                    'privCamType': priv_cam_type,
                                                                    'basic': basic,
                                                                    'streamInfo': stream_info,
                                                                    'blPrivilege': privilege,
                                                                    'camStm': cam_stm
                                                                }))

    """Get specific camera settings"""

    def get_info(self, camera_ids=(), priv_cam_type=3, include_deleted_cam=False, basic=False, stream_info=False,
                 optimize=False, ptz=False, event_detection=False, device_out_cap=False, fisheye=False, cam_app_info=False):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='GetInfo',
                                                                extra={
                                                                    'cameraIds': ",".join(camera_ids),
                                                                    'privCamType': priv_cam_type,
                                                                    'blIncludeDeletedCam': include_deleted_cam,
                                                                    'basic': basic,
                                                                    'streamInfo': stream_info,
                                                                    'optimize': optimize,
                                                                    'ptz': ptz,
                                                                    'eventDetection': event_detection,
                                                                    'deviceOutCap': device_out_cap,
                                                                    'fisheye': fisheye,
                                                                    'camAppInfo': cam_app_info
                                                                }))

    """Get all camera group information"""

    def list_group(self, offset=0, limit=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='ListGroup',
                                                                extra={
                                                                    'offset': offset,
                                                                    'limit': limit
                                                                }))

    """Get the up-to-date snapshot of the selected camera in JPEG format"""

    def get_snapshot(self, camera_id='', preview=False, cam_stm=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='GetSnapshot',
                                                                extra={
                                                                    'cameraId': camera_id,
                                                                    'preview': preview,
                                                                    'camStm': cam_stm
                                                                }))

    """Enable cameras"""

    def enable(self, camera_ids=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='Enable',
                                                                extra={
                                                                    'cameraIds': ",".join(camera_ids)
                                                                }))

    """Disable cameras"""

    def disable(self, camera_ids=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='Disable',
                                                                extra={
                                                                    'cameraIds': ",".join(camera_ids)
                                                                }))

    """Get capability of a specific camera by its camera Id"""

    def get_capability(self, camera_id=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='GetCapabilityByCamId',
                                                                extra={
                                                                    'cameraId': camera_id
                                                                }))

    """Enumerates current status of migration"""

    def migration_enum(self, start=0, limit='', owner_ds_id=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='MigrationEnum',
                                                                extra={
                                                                    'start': start,
                                                                    'limit': limit,
                                                                    'ownerDsId': owner_ds_id
                                                                }))

    """Migrating Cameras and recorded video (optional) to specified DS"""

    def migrate(self, server_id='', cam_id_list=(), del_mode=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='Migrate',
                                                                extra={
                                                                    'serverId': server_id,
                                                                    'camIdList': ",".join(cam_id_list),
                                                                    'delMode': del_mode
                                                                }))

    """This method lists groups along with number of cameras which belong to according to specified criteria"""

    def count_by_category(self, start=0, limit=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='CountByCategory',
                                                                extra={
                                                                    'start': start,
                                                                    'limit': limit
                                                                }))

    """To activate the "getOccupiedSize" API for real-time size-calculating"""

    def recount_event_size(self, cam_id=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='RecountEventSize',
                                                                extra={
                                                                    'camId': cam_id
                                                                }))

    """This method returns the occupied volume in GigaBytes"""

    def get_occupied_size(self, cam_id_list=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='GetOccupiedSize',
                                                                extra={
                                                                    'camIdList': ",".join(cam_id_list)
                                                                }))

    """Check if the shortcut item is valid"""

    def check_cam_valid(self, camera_id=''):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='CheckCamValid',
                                                                extra={
                                                                    'cameraId': camera_id
                                                                }))

    """Deleting selected tasks"""

    def migration_cancel(self, task_ids=()):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='MigrationCancel',
                                                                extra={
                                                                    'taskIds': ",".join(task_ids)
                                                                }))

    """Delete cameras"""

    def delete(self, camera_ids=(), keep_events=False):
        return self._api.req(self._api_name, self._api.endpoint(api=self._api_name,
                                                                cgi=self._cgi_path,
                                                                version=self._version,
                                                                method='Delete',
                                                                extra={
                                                                    'cameraIds': ",".join(camera_ids),
                                                                    'keepEvents': keep_events
                                                                }))

