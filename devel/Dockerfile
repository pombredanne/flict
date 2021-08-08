FROM python:3.6

# FOSS Compliance Utils / compliance-tool
#
# SPDX-FileCopyrightText: 2021 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later


#######################################################
#
# update main system
#
#######################################################
#RUN apt-get update && apt-get install -y bzip2 xz-utils zlib1g libxml2-dev libxslt1-dev p7zip-full jq
RUN  apt-get update && apt-get install -y jq
#python3-pip

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

#ENV PATH=$HOME/scancode-toolkit-${SCANCODE_VERSION}:$HOME/aboutcode-toolkit:$HOME/deltacode:$HOME/compliance-utils/bin:$HOME/scancode-manifestor:/usr/local/bin:/:/compliance-scripts/copyright-statements:$PATH

