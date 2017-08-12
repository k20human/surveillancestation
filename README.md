# Synology Surveillance Station API in Python

[![Build Status](https://travis-ci.org/k20human/surveillancestation.svg)](https://travis-ci.org/k20human/surveillancestation)

Python3 binding to Synology Surveillance API. I refer to the following document:
[Surveillance_Station_Web_API_v2.0.pdf](https://global.download.synology.com/download/Document/DeveloperGuide/Surveillance_Station_Web_API_v2.0.pdf).

## API coverage

### Implemented

| Endpoint                                      | Description                                                                                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------|
| SYNO.SurveillanceStation.Info                 | Retrieve Surveillance Station-related general information          |

### Partial

| Endpoint                                      | Description                                                                                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------|


### TODO

| Endpoint                                      | Description                                                                                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------|
| SYNO.SurveillanceStation.Camera               | Retrieve camera-related information                                |
| SYNO.SurveillanceStation.PTZ                  | Perform camera PTZ actions                                         |
| SYNO.SurveillanceStation.ExternalRecording    | Control external recording of cameras                              |
| SYNO.SurveillanceStation.Event                | Query event information                                            |
| SYNO.SurveillanceStation.Device               | Get information of Visual Station and CMS                          |
| SYNO.SurveillanceStation.Emap                 | Get information of defined E-Maps                                  |
| SYNO.SurveillanceStation.Streaming            | Get video stream of live view and recorded events                  |
| SYNO.SurveillanceStation.AudioStream          | Get audio stream of live view                                      |
| SYNO.SurveillanceStation.VideoStream          | Get video stream of live view                                      |
| SYNO.SurveillanceStation.Notification         | Get authorized token of DS                                         |

## Install

```bash
pip install [--upgrade] https://github.com/k20human/surveillancestation/tarball/master#egg=surveillance-station
```

## Usage
```python
# Create API
api = Api(host=config['host'], user=config['login'], passwd=config['password'])

# Create API Info
info = Info(api)

# Get Surveillance Station infos
print('Get info')
jsonprint(info.get_info())

# Don't forget to logout
api.logout()
```

## Inspiration

- https://github.com/satreix/synology ([sources](https://github.com/satreix/synology)) Python API for communication with Synology Filestation