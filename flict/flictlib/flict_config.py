###################################################################
#
# flict - FOSS License Compatibility Tool
#
# SPDX-FileCopyrightText: 2020 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
###################################################################

import os

flict_version = "0.1"

SCRIPT_DIR = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/../")

# TODO: replace this with something that makes installation easy
VAR_DIR = SCRIPT_DIR + "/var/"
DEFAULT_TRANSLATIONS_BASE_FILE = "translation.json"
DEFAULT_GROUP_BASE_FILE = "license-group.json"
DEFAULT_RELICENSE_BASE_FILE = "relicense.json"
DEFAULT_SCANCODE_BASE_FILE = "scancode-licenses.json"
DEFAULT_MATRIX_BASE_FILE = "osadl-matrix.csv"

DEFAULT_TRANSLATIONS_FILE = VAR_DIR + DEFAULT_TRANSLATIONS_BASE_FILE
DEFAULT_GROUP_FILE = VAR_DIR + DEFAULT_GROUP_BASE_FILE
DEFAULT_RELICENSE_FILE = VAR_DIR + DEFAULT_RELICENSE_BASE_FILE
DEFAULT_SCANCODE_FILE = VAR_DIR + DEFAULT_SCANCODE_BASE_FILE
DEFAULT_MATRIX_FILE = VAR_DIR + DEFAULT_MATRIX_BASE_FILE

