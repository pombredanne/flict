#!/usr/bin/python3

import subprocess
import yaml

YAML_FILE = '.github/workflows/push.yml'


def get_test_commands():
    ret = None
    with open(YAML_FILE, 'r') as file:
        documents = yaml.full_load(file)

        for item in documents['jobs']['build']['steps']:
            if 'name' in item and item['name'] == "Test":
                ret = str(item['run'])

    return ret

# flake8: noqa: S404
def run_command(command):
    ret_code = None
    try:
        res = subprocess.check_output("bash -c \"" + command + "\"", shell=True)
        print(str(res.decode("utf-8")))
    except Exception as e:
        print(str(res.decode("utf-8")))
        print("Tests failed....")
        exit(e.returncode)



command = get_test_commands().replace("tests\n", "tests &&").replace("\n", "")


if command is None:
    print("Wooops, could not extract command from " + YAML_FILE)
    exit(-1)

run_command(command)


