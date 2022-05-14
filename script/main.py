import json
import sys

args = sys.argv

json = json.loads(args[1])

for item in json:
    print(item)