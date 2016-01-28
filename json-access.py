from argparse import ArgumentParser
from lazyjson import load
import sys
from functools import reduce

parser = ArgumentParser("json-access")
parser.add_argument("keys", nargs = "*")
args = parser.parse_args()

keys = args.keys

for data in load(sys.stdin):
    if keys:
        for key in map(lambda key: key.split("."), keys):
            try:
                print(reduce(lambda value, subkey: value[subkey], key, data))
            except KeyError:
                pass
    else:
        print(data)
