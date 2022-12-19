#!/usr/bin/env python3
import requests
import json

dataKeys = ["d1","d2","d3","d4","d5","d6","d7"]

with open("./config.json") as f:
    conf = json.loads(f.read())

print(f"conf:{conf}")
channelId = conf["source"]["ambient_channel"]
readKey = conf["source"]["ambient_key_read"]

url = f"https://ambidata.io/api/v2/channels/{channelId}/data?&readKey={readKey}&n=1"

res = requests.get(url)
print(res.status_code)

d = res.json()[0]

data = {i:d[i] for i in d.keys() if i in dataKeys}

print(data)