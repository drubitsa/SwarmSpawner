OWNER=rasmunk
IMAGE=swarmspawner
TAG=devel

.PHONY: build

all: clean build push

build:
	docker build -t ${OWNER}/${IMAGE}:${TAG} .

clean:
	docker rmi -f ${OWNER}/${IMAGE}:${TAG}

push:
	docker push ${OWNER}/${IMAGE}:${TAG}
