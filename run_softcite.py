import os
import sys
import requests
from glob import glob


def run_softcite(config_path, file):
    softcite_up = requests.get("http://localhost:8060").status_code == 200
    if softcite_up:
        # Ne s'execute pas sur des pdfs compressés (.gz) -> config_harvester compression: false
        client = smc.software_mention_client(config_path)
        client.annotate(file, file.replace('pdf', 'json'), None)
        client.diagnostic(full_diagnostic=False)


if __name__ == "__main__":
    sys.path.insert(1, os.path.join(sys.path[0], '..'))
    from software_mentions_client import software_mention_client as smc

    config_path_softcite = './config/config_softcite.json'
    dest_dir = './tmp/downloaded_publications/'
    file = glob('./tmp/downloaded_publications/*.pdf')[0]
    run_softcite(config_path_softcite, file)

