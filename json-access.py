from argparse import ArgumentParser
from json import loads
import sys

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
                value = data[key[0]]
                for subkey in key[1:]:
                    value = value[subkey]
                print(value)
            except KeyError:
                pass
    else:
        print(data)
