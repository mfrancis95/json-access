from argparse import ArgumentParser
from json import load
import sys

parser = ArgumentParser("json-access")
parser.add_argument("key")
args = parser.parse_args()

print(load(sys.stdin)[args.key])
