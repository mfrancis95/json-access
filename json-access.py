from argparse import ArgumentParser
from json import load
import sys

parser = ArgumentParser("json-access")
parser.add_argument("keys", nargs = "+")
args = parser.parse_args()

json = load(sys.stdin)

for key in map(lambda key: key.split("."), args.keys):
    try:
        value = json[key[0]]
        for subkey in key[1:]:
            value = value[subkey]
        print(value)
    except KeyError:
        pass
