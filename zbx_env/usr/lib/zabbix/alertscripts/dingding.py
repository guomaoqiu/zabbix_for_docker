#!/usr/bin/python
# Author: guomaoqiu
# QQ: 2399447849
# Email: 2399447849@qq.com
# Describe: 钉钉webhook

import requests
import json
import sys
import os
 
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=e832a6d764324fa5c961c4fce72319734fc614513be9ee00f0234c334b939372"
 
def msg(text):
    json_text= {
     "msgtype": "text",
        "at": {
            "atMobiles": [
               "13524894451"
            ],
            "isAtAll": True
        },
        "text": {
            "content": text
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
