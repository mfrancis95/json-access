from argparse import ArgumentParser
from json import load
import sys

parser = ArgumentParser("json-access")
parser.add_argument("keys", nargs = "+")
args = parser.parse_args()

json = load(sys.stdin)

for key in args.keys:
    value = json.get(key)
    if value is not None:
        print(value)
