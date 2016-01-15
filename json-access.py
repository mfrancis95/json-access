from argparse import ArgumentParser
import json
import sys

parser = ArgumentParser("json-access")
parser.add_argument("keys", nargs = "*")
args = parser.parse_args()

keys = args.keys
data = json.load(sys.stdin)

if keys:
    for key in map(lambda key: key.split("."), args.keys):
        try:
            value = data[key[0]]
            for subkey in key[1:]:
                value = value[subkey]
            print(value)
        except KeyError:
            pass
else:
    print(data)
