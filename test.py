#!python3

import json
import fastjsonschema

with open('schemas/asset-v1.0.json') as fd:
    data = json.load(fd)

fastjsonschema.compile(data)
