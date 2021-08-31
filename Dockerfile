# SPDX-FileCopyrightText: 2021 Jens Erdmann
#
# SPDX-License-Identifier: GPL-3.0-or-later

FROM python:3-slim
ARG INSTALL_TEST=0

WORKDIR /opt/flict

#TODO: We might want to clean this up after install or in final image.
COPY . .

RUN INSTALL_TEST=${INSTALL_TEST} ./install.sh

ENTRYPOINT [ "flict" ]
