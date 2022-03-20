#!python3

import json
import fastjsonschema

with open('schemas/asset.json') as fd:
    data = json.load(fd)

fastjsonschema.compile(data)


