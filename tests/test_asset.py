#!python3

import json
import fastjsonschema
import unittest


class TestAccountManager(unittest.TestCase):
    def test_asset(self):
        with open('schemas/asset-v0.1.json') as fd:
            data = json.load(fd)

        fastjsonschema.compile(data)


if __name__ == '__main__':
    unittest.main()
