#!/usr/bin/python

# This should be place inside gotify backends directory
#   - ~/.local/lib/python3.8/site-packages/ntfy/backends/gotify.py

import requests
import json

from ..config import USER_AGENT

GOTIFY_MSG_URL = '{url}/message?token={token}'


def notify(title,
           message,
           url,
           access_token,
           extras=None,
           priority=None,
           retcode=None):
    """
    Required parameter:
        * ``url`` - The url of the gotify server
        * ``access_token`` - Your Gotify App access token

    Optional parameters:
        * ``priority`` - integer
        * ``extras`` - Additional data in json format sent along the message

    For more info, see: https://gotify.net/docs
    """

    data = {
        'title': title,
        'message': message,
    }

    if priority is not None:
        data['priority'] = priority

    if extras is not None:
        if type(extras) == dict:
            data['extras'] = extras
        elif type(extras) == str:
            data['extras'] = json.loads(extras.replace("'", '"'))
        else:
            raise Exception('"extras" argument must be a string or a dictionary')

    headers = {'User-Agent': USER_AGENT}

    resp = requests.post(
        GOTIFY_MSG_URL.format(url=url, token=access_token),
        json=data,
        headers=headers
    )

    resp.raise_for_status()
