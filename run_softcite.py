import os
import sys
import requests
from glob import glob
from config.path_config import DATA_PATH, CONFIG_PATH_SOFTCITE


def run_softcite(config_path, data_path):
    # Ne s'execute pas sur des pdfs compressés (.gz) -> config_harvester compression: false
    client = smc.software_mention_client(config_path)
    client.annotate_directory(data_path)
    client.diagnostic(full_diagnostic=False)


if __name__ == "__main__":
    sys.path.insert(1, os.path.join(sys.path[0], '..'))
    from software_mentions_client import software_mention_client as smc

    run_softcite(CONFIG_PATH_SOFTCITE, DATA_PATH)

