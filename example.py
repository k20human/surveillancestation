#!/usr/bin/python3

import logging

from surveillancestation.api import Api
from surveillancestation.info import Info
from surveillancestation.utils import jsonprint

import json
import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# Configuration file path
configurationFile = './config.json'

# Configure logs
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

file_handler = RotatingFileHandler('linky.log', 'a', 1000000, 1)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.INFO)
steam_handler.setFormatter(formatter)
logger.addHandler(steam_handler)

# Check if configuration file exists
if os.path.isfile(configurationFile):
    # Import configuration file
    with open(configurationFile) as data_file:
        config = json.load(data_file)
else:
    logger.error('Your configuration file doesn\'t exists')
    sys.exit('Your configuration file doesn\'t exists')

# Create API
api = Api(host=config['host'], user=config['login'], passwd=config['password'])

# Create API Info
info = Info(api)

# Get Surveillance Station infos
print('Get info')
jsonprint(info.get_info())

# Don't forget to logout
api.logout()
