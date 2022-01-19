DOCKER_IMAGE_NAME=dataesr/bso3-process-publication
CURRENT_VERSION=$(shell cat application/__init__.py | cut -d "'" -f 2)

all: 
	@make download_file_from_ovh
	@make process_pipeline
	@make upload_file_to_ovh

process_pipeline:
	@make run_softcite
	@make run_grobid

run_grobid: run_grobid.py
	@python run_grobid.py

run_softcite: run_softcite.py
	@python run_softcite.py

upload_file_to_ovh: ovh_handler.py
	@python ovh_handler.py --upload

download_file_from_ovh: ovh_handler.py
	@python ovh_handler.py --download

clean:
	@rm -rf ./tmp/downloaded_publications
	@rm -rf *pdf
	@rm -rf *gz
	@rm -rf ./lmdb/entries_software

docker-build:
	@echo Building a new docker image
	docker build --no-cache -t $(DOCKER_IMAGE_NAME):$(CURRENT_VERSION) -t $(DOCKER_IMAGE_NAME):latest .
	@echo Docker image built

docker-run:
	@echo Running the created docker image in a container
	docker run $(DOCKER_IMAGE_NAME):latest

docker-push:
	@echo Pushing a new docker image
	docker push $(DOCKER_IMAGE_NAME):$(CURRENT_VERSION)
	docker push $(DOCKER_IMAGE_NAME):latest
	@echo Docker image pushed

install:
	@echo Installing dependencies...
	pip install -r requirements.txt
	@echo End of dependencies installation
