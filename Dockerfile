# SPDX-FileCopyrightText: 2021 Jens Erdmann
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Multi-Stage Docker Image
#
# Using a multi-stage docker image to derive a test image from the main
# image to run tests in but not affect the production image.

FROM python:3-slim as flict-base

#TODO: This should be a variable as it is used on different occations.
WORKDIR /opt/flict

#TODO: We might want to clean this up after install or in final image.
COPY . .

RUN python3 -m pip install -r requirements.txt \
 && python3 setup.py build \
 && python3 setup.py install

ENTRYPOINT [ "flict" ]

# Declare testing image for testing purposes.
# Use --target flict-test to build this part.
FROM flict-base as flict-test

RUN python3 -m pip install -r requirements-dev.txt

ENTRYPOINT [ "/bin/sh", "-c", "/opt/flict/tests/all.sh" ]


# declare final image
FROM flict-base 

# This part is empty as everything is already set up by the base image.
