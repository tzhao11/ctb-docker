# -*- coding: utf-8 -*-

DEBUG_MODE = True  # log will not take up much place, but it is necessary when locating problems

BAIDU_API = 'asdasdaasd'

# cq-http-api server config
API_ROOT = 'http://coolq:5700/'  # should be the same as cq-http-api api address
ACCESS_TOKEN = ''  # should be the same as cq-http-api config
SECRET = ''  # should be the same as cq-http-api config

# cq-http-api client config, should be the same as cq-http-api post config
HOST = '0.0.0.0'
PORT = 8080

TOKEN = 'your-telegram-bot-token'
QQ_BOT_ID = 'your-qq-bot-id'
FORWARD_LIST = [
    {
        'QQ': 12345678,
        'TG': -12345678,
        'DRIVE_MODE': False,
        'IMAGE_LINK': False
    },
]
SERVER_PIC_URL = ''
CQ_ROOT = r'/coolq'
