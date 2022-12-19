#!/usr/bin/env python3
import requests

dataKeys = ["d1","d2","d3","d4","d5","d6","d7"]

channelId = 12345
readKey = "hoge"

url = f"https://ambidata.io/api/v2/channels/{channelId}/data?&readKey={readKey}&n=1"

res = requests.get(url)
print(res.status_code)

d = res.json()[0]

data = {i:d[i] for i in d.keys() if i in dataKeys}

print(data)