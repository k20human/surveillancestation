# Synology Surveillance Station API in Python

[![Build Status](https://travis-ci.org/k20human/surveillancestation.svg)](https://travis-ci.org/k20human/surveillancestation)

Python3 binding to Synology Surveillance API. I refer to the following document:
[Surveillance_Station_Web_API_v2.0.pdf](https://global.download.synology.com/download/Document/DeveloperGuide/Surveillance_Station_Web_API_v2.0.pdf).

## API coverage

### Implemented

| Endpoint                                      | Description                                                        |
|-----------------------------------------------|--------------------------------------------------------------------|
| SYNO.SurveillanceStation.Info                 | Retrieve Surveillance Station-related general information          |

### Partial

| Endpoint                                      | Description                                         | Missing                          |
|-----------------------------------------------|-----------------------------------------------------|----------------------------------|
| SYNO.SurveillanceStation.Camera               | Retrieve camera-related information                 | SaveOptimizeParam, *SYNO.SurveillanceStation.Camera.Event*, *SYNO.SurveillanceStation.Camera.Import* |
| SYNO.SurveillanceStation.ActionRule           | Provides a method to acquire information of ActionRule |  |
| SYNO.SurveillanceStation.Notification         | Control notification                               | *SYNO.SurveillanceStation.Notification.SMS*, *SYNO.SurveillanceStation.Notification.PushService*, *SYNO.SurveillanceStation.Notification.Email*, *SYNO.SurveillanceStation.Notification.Filter* |

### TODO

| Endpoint                                      | Description                                                        |
|-----------------------------------------------|--------------------------------------------------------------------|
| SYNO.SurveillanceStation.PTZ                  | Perform camera PTZ actions                                         |
| SYNO.SurveillanceStation.ExternalRecording    | Control external recording of cameras                              |
| SYNO.SurveillanceStation.Event                | Query event information                                            |
| SYNO.SurveillanceStation.Device               | Get information of Visual Station and CMS                          |
| SYNO.SurveillanceStation.Emap                 | Get information of defined E-Maps                                  |
| SYNO.SurveillanceStation.Streaming            | Get video stream of live view and recorded events                  |
| SYNO.SurveillanceStation.AudioStream          | Get audio stream of live view                                      |
| SYNO.SurveillanceStation.VideoStream          | Get video stream of live view                                      |

## Install

```bash
pip install [--upgrade] https://github.com/k20human/surveillancestation/tarball/master#egg=surveillance-station
```

## Usage
```python
# Create API
api = Surveillancestation(host=config['host'], user=config['login'], passwd=config['password'])

# Get Surveillance Station infos
print('Get info')
jsonprint(api.info.get_info())

# Don't forget to logout
api.logout()
```

## Inspiration

- https://github.com/satreix/synology ([sources](https://github.com/satreix/synology)) Python API for communication with Synology Filestation
