all: 
	make download_file_from_ovh
	make process_pipeline
	make upload_file_to_ovh

process_pipeline:
	make run_softcite
	make run_grobid

run_grobid: run_grobid.py
	python run_grobid.py

run_softcite: run_softcite.py
	python run_softcite.py

upload_file_to_ovh: ovh_handler.py
	python ovh_handler.py --upload

download_file_from_ovh: ovh_handler.py
	python ovh_handler.py --download

clean:
	rm -rf ./tmp/downloaded_publications