import os
import sys
import requests
from glob import glob


def run_grobid(config_path, data_path):
    grobid_up = requests.get("http://localhost:8070").status_code == 200
    if grobid_up:
        client = GrobidClient(config_path=config_path)
        client.process("processFulltextDocument", data_path, output=f"{data_path}/grobid_out/", consolidate_citations=True, tei_coordinates=True, force=True, verbose=True, n=4)


if __name__ == "__main__":
    sys.path.insert(1, os.path.join(sys.path[0], '..'))
    from grobid_client.grobid_client import GrobidClient

    config_path_grobid = './config/config_grobid.json'
    dest_dir = './tmp/downloaded_publications/'
    file = glob('./tmp/downloaded_publications/*.pdf')[0]
    run_grobid(config_path_grobid, dest_dir)

