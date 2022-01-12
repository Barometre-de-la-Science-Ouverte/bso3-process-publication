import os

# Paths
PROJECT_DIRNAME = os.path.dirname(os.path.dirname(__file__))
# CONFIG_PATH = os.path.join(PROJECT_DIRNAME, 'config.json')
# PMC_PATH = os.path.join(os.path.dirname(PROJECT_DIRNAME), 'oa_file_list.txt')
DATA_PATH = os.path.join(PROJECT_DIRNAME, 'tmp/downloaded_publications/')
LOG_PATH = os.path.join(PROJECT_DIRNAME, os.path.join('logs', 'logger.log'))
CONFIG_PATH_GROBID = os.path.join(PROJECT_DIRNAME, 'config/config_grobid.json')
CONFIG_PATH_SOFTCITE = os.path.join(PROJECT_DIRNAME, 'config/config_softcite.json')
CONFIG_PATH_OVH = os.path.join(PROJECT_DIRNAME, 'config/config_ovh.json')

# Urls
OVH_AUTH_URL = 'https://auth.cloud.ovh.net/v3'