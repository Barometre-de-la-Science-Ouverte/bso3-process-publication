import argparse
import json
import os
import swift
from glob import glob
from config.path_config import CONFIG_PATH_OVH, DATA_PATH


def generateStoragePath(identifier):
    """Convert a file name into a path with file prefix as directory paths:
    123456789 -> 12/34/56/78/123456789"""
    return os.path.join(identifier[:2], identifier[2:4], identifier[4:6], identifier[6:8], identifier)


def download_files(_swift, dest_dir):
    files = _swift.get_swift_list()
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    return _swift.download_files(files, dest_dir)


def upload_and_clean_up(_swift, local_dir):
    files = glob(local_dir + '*')
    upload_files = [(file, generateStoragePath(os.path.basename(file)))
        for file in files if not (file.endswith('.pdf') or file.endswith('.pdf.gz'))]
    _swift.upload_files_to_swift(upload_files)
    for file in files:
        os.remove(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--upload", action="store_true")
    args = parser.parse_args()
    upload = args.upload
    download = args.download
    
    config_harvester = json.load(open(CONFIG_PATH_OVH,'r'))
    _swift = swift.Swift(config_harvester)
    if download:
        download_files(_swift, DATA_PATH)
    if upload:
        upload_and_clean_up(_swift, DATA_PATH)