# FOSS Compliance Utils
#
# SPDX-FileCopyrightText: 2021 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

CONTAINER_NAME=flict-devel
IMAGE_NAME=vinland/${CONTAINER_NAME}

MOUNT_DIR=/compliance-tools
TAG=`grep flict_version ../flict/flictlib/flict_config.py | cut -d '"' -f 2`

test:
	make docker-wipe build

check:
	@echo "IMAGE_NAME:     $(IMAGE_NAME)"
	@echo "CONTAINER_NAME: $(CONTAINER_NAME)"
	@echo "TAG:            $(TAG)"

run:
	docker run -it --rm -name $(CONTAINER_NAME) $(IMAGE_NAME):$(TAG) uname -a

build:
	docker build `pwd` -t $(IMAGE_NAME):$(TAG)

nc-build:
	docker build --no-cache `pwd` -t $(IMAGE_NAME):$(TAG)

docker-wipe-c:
	for c in `docker container ps -a |  grep $(CONTAINER_NAME) | awk '{print $$1}' | grep -v CONTA `; do docker container rm -f $$c; done

docker-wipe-i:
	for i in `docker image ls -a | grep $(CONTAINER_NAME) | awk ' {print $$3} ' | grep -v IMA `; do docker image rm -f $$i ; done

docker-wipe: docker-wipe-c docker-wipe-i

docker-show:
	@echo 
	@docker image ls -a
	@echo 
	@docker container ls -a
	@echo 
	@docker container ps -a

size:
	@echo "Containers "
	@echo "===================================="
	docker ps -as
	@echo "Images"
	@echo "===================================="
	docker images

