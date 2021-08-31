#!/bin/sh

# SPDX-FileCopyrightText: 2021 Jens Erdmann
#
# SPDX-License-Identifier: GPL-3.0-or-later


echo "Installing dependencies ..."
python3 -m pip install -r requirements.txt

# INSTALL_TEST is substituted with 0 if not set or set but empty
if [ "${INSTALL_TEST:-0}" -eq "1" ]; then
    echo "Installing test dependencies ..."
    python3 -m pip install -r requirements-dev.txt
fi

echo "Building module ..."
python3 setup.py build

echo "Installing module .."
python3 setup.py install
