#!/usr/bin/env python
import json
import yaml
import argparse

parser = argparse.ArgumentParser(description="Convert YAML to JSON")
parser.add_argument('-i', '--input', help="input YAML file",
                    dest='yaml_in', required=True)
parser.add_argument('-o', '--output', help="output JSON file name",
                    dest='json_out', required=True)
args = parser.parse_args()
with open(args.yaml_in, 'r') as fy:
    with open(args.json_out, 'w') as fj:
        print json.dump(yaml.load(fy.read()), fj, sort_keys=True, indent=2)
