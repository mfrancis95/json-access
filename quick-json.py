from argparse import ArgumentParser
from lazyjson import load
from json import dumps
import sys
from functools import reduce

parser = ArgumentParser("json-access")
parser.add_argument("-f", "--file")
parser.add_argument("-i", "--indent", default = 4, type = int)
subparsers = parser.add_subparsers(dest = "command")

getparser = subparsers.add_parser("get")
getparser.add_argument("keys", nargs = "*")

removeparser = subparsers.add_parser("remove")
removeparser.add_argument("keys", nargs = "+")

args = parser.parse_args()
indent = args.indent
keys = list(map(lambda key: key.split("."), args.keys))

def json_get(file):
    for json in load(file):
        if keys:
            for key in keys:
                try:
                    print(dumps(reduce(lambda value, subkey: value[subkey], key, json), indent = indent))
                except KeyError:
                    pass
        else:
            print(dumps(json, indent = indent))

def json_remove(file):
    for json in load(file):
        for key in keys:
            try:
                remove = json
                last_key_index = len(key) - 1
                for i in range(last_key_index):
                    remove = remove[key[i]]
                del remove[key[last_key_index]]
            except KeyError:
                pass
    print(dumps(json, indent = indent))

file = args.file
if file:
    with open(file) as f:
        (json_get if args.command == "get" else json_remove)(f)
else:
    (json_get if args.command == "get" else json_remove)(sys.stdin)
