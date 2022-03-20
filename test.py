#!python3

import json
import fastjsonschema

with open('schemas/asset-v0.1.json') as fd:
    data = json.load(fd)

fastjsonschema.compile(data)
