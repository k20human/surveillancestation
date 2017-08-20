import json
import logging
import requests
import urllib3

from .errors import errors


class Api:
    def __init__(self, host, user, passwd):
        self._host = host
        self._user = user
        self._passwd = passwd
        self._sid = ''
        self._logged_in = False
        self._session_name = 'SurveillanceStation'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self._login()

    def _login(self):
        data = self.req('SYNO.API.Info', self.endpoint('SYNO.API.Info',
                                      query='SYNO.API.Auth,SYNO.SurveillanceStation.'))
        login_endpoint = self.endpoint(
            'SYNO.API.Auth',
            version=str(data['SYNO.API.Auth']['maxVersion']),
            cgi=data['SYNO.API.Auth']['path'],
            method='login',
            extra={
                'account': self._user,
                'passwd': self._passwd,
                'session': self._session_name,
                'format': 'sid'
            }
        )
        data2 = self.req('SYNO.API.Auth', login_endpoint)
        if not 'code' in data2:
            self._sid = data2['sid']
            self._logged_in = True

    def _base_endpoint(self, cgi):
        ret = self._host + '/webapi/' + cgi
        return ret

    def _get_response_data(self, api_name, response):
        if response.status_code != 200:
            logging.error('HTTP status: ' + str(response.status_code))

        # Status 500
        if response.status_code == 500:
            return {'Error': errors[500]}

        try:
            response_json = response.json()
        except json.JSONDecodeError:
            return response.content

        if response_json['success'] == True:
            if 'data' in response_json.keys():
                return response_json['data']
            return ''

        # Get error message
        code = response_json['error']['code']
        if code in errors:
            error_message = errors[code]
        elif api_name in errors and code in errors[api_name]:
            error_message = errors[api_name][code]
        else:
            error_message = str(response_json['error']['code'])

        logging.error('failure - ' + str(response_json['error']['code']) + ' - ' + error_message)
        return response_json['error']

    def _is_response_binary(self, response):
        return 'text/plain' not in response.headers['content-type']

    def get_max_version(self, api):
        data = self.req('SYNO.API.Info', self.endpoint('SYNO.API.Info',
                                      query=api))
        return str(data[api]['maxVersion'])

    def logout(self):
        logout_endpoint = self.endpoint(
            'SYNO.API.Auth',
            cgi='auth.cgi',
            method='logout',
            extra={'session': self._session_name}
        )
        self.req('SYNO.API.Auth', logout_endpoint)

    def endpoint(self, api, query='', cgi='query.cgi', version='1', method='query', extra={}):
        ret = self._base_endpoint(cgi) + '?api=' + api + '&version=' + str(version) + '&method=' + method

        if query:
            ret += '&query=' + query

        for key, value in extra.items():
            if value:
                if isinstance(value, dict):
                   value = json.dumps(value)
                else:
                    value = str(value)

                ret += '&' + key + '=' + str(value)


        if self._sid:
            ret += '&_sid=' + self._sid

        return ret

    def req(self, api_name, endpoint):
        logging.info('GET: ' + endpoint)
        r = requests.get(endpoint, verify=False)

        return self._get_response_data(api_name, r)

    def req_binary(self, api_name, endpoint, **kw):
        logging.info('GET: ' + endpoint)
        r = requests.get(endpoint, **kw)

        if self._is_response_binary(r):
            if "stream" in kw:
                return r
            else:
                return r.content

        self._get_response_data(api_name, r)

        return None

    def req_post(self, api_name, endpoint, data, files):
        logging.info('url: ' + endpoint)
        try:
            r = requests.post(endpoint, verify=False, data=data, files=files)
        except:
            return None

        return self._get_response_data(api_name, r)
