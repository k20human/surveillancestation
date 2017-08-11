# surveillance-station
Synology Surveillance Station API in Python

# Synology Surveillance Station API in Python

[![Build Status](https://travis-ci.org/k20human/surveillance-station.svg)](https://travis-ci.org/k20human/surveillance-station)

Python3 binding to Synology Surveillance API. I refer to the following document:
[Surveillance_Station_Web_API_v2.0.pdf](https://global.download.synology.com/download/Document/DeveloperGuide/Surveillance_Station_Web_API_v2.0.pdf).

## API coverage

### Implemented

| Endpoint                                      | Description                                                                                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------|

### Partial

| Endpoint                                      | Description                                                                                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------|


### TODO

| Endpoint                                      | Description                                                                                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------|
| SYNO.API.Info                                 | Discover all API information                                       |
| SYNO.API.Auth                                 | Perform session login and logout                                   |
| SYNO.SurveillanceStation.Info                 | Retrieve Surveillance Station-related general information          |
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
pip install [--upgrade] https://github.com/k20human/surveillance-station/tarball/master#egg=surveillance-station
```

## Usage
```python

```

## Other implementations

- https://github.com/satreix/synology ([sources](https://github.com/satreix/synology)) Python API for communication with Synology Filestation