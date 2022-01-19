import json
from config.path_config import (CONFIG_PATH_OVH, CONFIG_PATH_GROBID,
                                CONFIG_PATH_SOFTCITE, DATA_PATH)
import swift
from ovh_handler import download_files, upload_and_clean_up
from run_grobid import run_grobid
from run_softcite import run_softcite
from software_mentions_client.client import software_mentions_client as smc
from grobid_client.grobid_client import GrobidClient


def main():
    config_harvester = json.load(open(CONFIG_PATH_OVH,'r'))
    _swift = swift.Swift(config_harvester)
    download_files(_swift, DATA_PATH)
    run_grobid(CONFIG_PATH_GROBID, DATA_PATH, GrobidClient)
    run_softcite(CONFIG_PATH_SOFTCITE, DATA_PATH, smc)
    upload_and_clean_up(_swift, DATA_PATH)

if __name__ == "__main__":
    main()
