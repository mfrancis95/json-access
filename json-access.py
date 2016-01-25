from argparse import ArgumentParser
from json import loads
import sys
from functools import reduce

parser = ArgumentParser("json-access")
parser.add_argument("keys", nargs = "*")
args = parser.parse_args()

def lazyload(file):
    buffer = ""
    for line in file:
        buffer += line
        try:
            yield loads(buffer)
            buffer = ""
        except ValueError:
            pass

keys = args.keys

for data in lazyload(sys.stdin):
    if keys:
        for key in map(lambda key: key.split("."), keys):
            try:
                print(reduce(lambda value, subkey: value[subkey], key, data))
            except KeyError:
                pass
    else:
        print(data)
