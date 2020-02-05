#!/usr/bin/env python
import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Shodan Subdomain Finder by SmoZy\n\nUsage: ./shodan.py [API Key] [Domain]"
        sys.exit(1)

apikey = sys.argv[1]
domain = sys.argv[2]
_ = []

r = requests.get('https://api.shodan.io/dns/domain/' + domain + '?key=' + apikey)
data = json.loads(r.text)
for item in data["data"]:
    entry = item["subdomain"]
    record_type = item["type"]
    value = item["value"]
    if record_type == 'CNAME' and domain in value:
        delim = value.split('.')
        match = delim[-2] + '.' + delim[-1]
        if match == domain:
            _.append(value)
final = set(_)
for x in final:
    print x
