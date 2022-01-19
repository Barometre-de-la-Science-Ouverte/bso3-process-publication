import json
import os
import sys

import swift
from config.path_config import (CONFIG_PATH_GROBID, CONFIG_PATH_OVH,
                                CONFIG_PATH_SOFTCITE, DATA_PATH,
                                PROJECT_DIRNAME)
from flask import Flask, jsonify
from ovh_handler import download_files, upload_and_clean_up
from run_grobid import run_grobid
from run_softcite import run_softcite

# sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(PROJECT_DIRNAME)))
# from grobid_client.grobid_client import GrobidClient
# from software_mentions_client import software_mention_client as smc

app = Flask(__name__)

@app.route('/process', methods=['GET'])
def run_task_process():
    """
    Download data from bso3_publications_dump, run grobid and softcite, upload generated files
    """
    config_harvester = json.load(open(CONFIG_PATH_OVH,'r'))
    _swift = swift.Swift(config_harvester)
    download_files(_swift, DATA_PATH)
    run_grobid(CONFIG_PATH_GROBID, DATA_PATH, GrobidClient)
    run_softcite(CONFIG_PATH_SOFTCITE, DATA_PATH, smc)
    upload_and_clean_up(_swift, DATA_PATH)
    """
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue('unpaywall', default_timeout=DEFAULT_TIMEOUT)
        task = q.enqueue(harvester.harvestUnpaywall, archive_path)
    """
    response_object = {
        'status': 'success'
    }

    return jsonify(response_object), 202


"""
@main_blueprint.route('/unpaywall/tasks/<task_id>', methods=['GET'])
def get_status(task_id):
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue('unpaywall')
        task = q.fetch_job(task_id)
    if task:
        response_object = {
            'status': 'success',
            'data': {
                'task_id': task.get_id(),
                'task_status': task.get_status(),
                'task_result': task.result,
            }
        }
    else:
        response_object = {'status': 'error'}
    return jsonify(response_object)
"""
