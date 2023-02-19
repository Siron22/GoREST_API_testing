from configparser import ConfigParser
import os

def get_root_directory():
    return os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]


def get_config():
    config = ConfigParser()
    config.read(os.path.join(get_root_directory(), 'config.ini'))
    return config


def get_base_url():
    return get_config().get('project', 'base_url')


def get_api_version():
    return get_config().get('project', 'api_version')


def get_headers_with_autorization():
    return eval(get_config().get('project', 'header_with_authorization'))


