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

putparser = subparsers.add_parser("put")
putparser.add_argument("key")
putparser.add_argument("value")

removeparser = subparsers.add_parser("remove")
removeparser.add_argument("keys", nargs = "+")

args = parser.parse_args()
indent = args.indent
command = args.command

def json_get(file):
    keys = list(map(lambda key: key.split("."), args.keys))
    for json in load(file):
        if keys:
            for subkeys in keys:
                try:
                    print(dumps(reduce(lambda get, subkey: get[subkey], subkeys, json), indent = indent))
                except:
                    pass
        else:
            print(dumps(json, indent = indent))

def json_put(file):
    subkeys = args.key.split(".")
    value = args.value
    last_index = len(subkeys) - 1
    last_subkey = subkeys[last_index]
    for json in load(file):
        try:
            put = json
            for i in range(last_index):
                put = put[subkeys[i]]
            put[last_subkey] = value
        except:
            pass
        print(dumps(json, indent = indent))

def json_remove(file):
    keys = list(map(lambda key: key.split("."), args.keys))
    for json in load(file):
        for subkeys in keys:
            try:
                remove = json
                last_index = len(subkeys) - 1
                for i in range(last_index):
                    remove = remove[subkeys[i]]
                del remove[subkeys[last_index]]
            except:
                pass
    print(dumps(json, indent = indent))

if command == "get":
    command = json_get
elif command == "put":
    command = json_put
else:
    command = json_remove

file = args.file
if file:
    with open(file) as f:
        command(f)
else:
    command(sys.stdin)
