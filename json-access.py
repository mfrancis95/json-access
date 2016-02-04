from argparse import ArgumentParser
from lazyjson import load
from json import dumps
import sys
from functools import reduce

parser = ArgumentParser("json-access")
parser.add_argument("-f", "--file")
parser.add_argument("-i", "--indent", default = 4, type = int)
parser.add_argument("keys", nargs = "*")
args = parser.parse_args()

indent = args.indent

def print_json(file, keys):
    for json in load(file):
        if keys:
            for key in map(lambda key: key.split("."), keys):
                try:
                    print(dumps(reduce(lambda value, subkey: value[subkey], key, json), indent = indent))
                except KeyError:
                    pass
        else:
            print(dumps(json, indent = indent))

file = args.file
if file:
    with open(file) as f:
        print_json(f, args.keys)
else:
    print_json(sys.stdin, args.keys)
