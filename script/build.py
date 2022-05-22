import json
import os
import subprocess
import argparse
from pathlib import Path
# from jsonschema import validate, ValidationError

parser = argparse.ArgumentParser()
parser.add_argument("-t","--target", type=str,required=True, help="target")
args = parser.parse_args()

target= args.target

with open('apps.json','r') as fh:
  build_json =json.load(fh)

# linux -> app1, app2
## -t linux -e BUILD_APPLICATIONS='app1,app2'

BUILD_APPLICATIONS=[]
for build_item in build_json['apps']:
  if target in str(build_item['target']).lower() and \
      str(build_item['enable']).lower() == "true":
    BUILD_APPLICATIONS.append(build_item['name'])


print(BUILD_APPLICATIONS)

os.environ['BUILD_APPLICATIONS']=" ".join(BUILD_APPLICATIONS)
cmd = subprocess.run("bash build.sh",shell=True)

