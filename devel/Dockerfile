FROM python:3.6

# flict
#
# SPDX-FileCopyrightText: 2021 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later


#######################################################
#
# update main system
#
#######################################################

RUN  apt-get update && apt-get install -y jq

#######################################################
#
# Flict
#
#######################################################

RUN echo && echo "---=== Installing pip ===---" && echo
RUN python3 -m pip install --upgrade pip

RUN echo && echo "---=== Cloning repository ===---" && echo
RUN git clone https://github.com/vinland-technology/flict.git 

RUN echo && echo "---=== Installing requirements ===---" && echo
RUN cd flict && pip install -r requirements.txt

RUN echo && echo "---=== Installing flict ===---" && echo
RUN cd flict && python3 setup.py install && flict --version

RUN echo && echo "---=== Installing development requirements ===---" && echo
RUN cd flict && pip install -r requirements-dev.txt 

RUN echo && echo "---=== Testing ===---" && echo
RUN cd flict/tests && ./all.sh
