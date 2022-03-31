import os
import yaml


class Config(object):

    def __init__(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(THIS_FOLDER, 'config.yml')
        with open(path, 'r') as ymlfile:
            self._config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        paths = self._get_property('model_path')
        for key in paths.keys():
            paths[key] = self._get_property('model_dir') + paths[key]
        self._config['model_path'] = paths


    @property
    def ground_truth(self):
        return self._get_property('ground_truth')

    @property
    def query_log(self):
        return self._get_property('query_log')

    def _get_property(self, property_name):
        if property_name not in self._config.keys():  # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]

