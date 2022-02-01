import argparse
import json
import sys 
import urllib.request
from typing import Text

import argparse
import sys 

def get_configpath():
    parser = argparse.ArgumentParser(
        description='TO get the cat facts from catfacts.ninja API'
    )
    parser.add_argument('-c', '--config', help='enter the path of config file', type=str, required=True)

    args = parser.parse_args()
    return args.config

def get_config():
    config_path = get_configpath()

    sys.path.append('..')
    from config.configfile import ConfigParser

    config_path = get_configpath()
    return ConfigParser(config_path).configdata


def get_fact(fact_url: Text, fact_file: Text):
    with urllib.request.urlopen(fact_url) as request:
        response_json = request.read()
        response = json.loads(response_json)

    with open(fact_file, 'w') as file:
        for each in response['data']:
            file.write(each['fact'] + '\n')

if __name__ == '__main__':
    configdata = get_config()
    MAX_FACTS = configdata['max_facts']
    FACT_URL = configdata['fact_url'] + str(MAX_FACTS) 
    FACT_FILE = configdata['fact_file']
    get_fact(FACT_URL, FACT_FILE)