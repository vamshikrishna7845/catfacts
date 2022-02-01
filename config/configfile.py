import yaml


class ConfigParser:
    def __init__(self, configfile='config.yaml') -> None:
        self.configfile = configfile
        self.configdata = self.get_config_information()

    def get_config_information(self):
        with open(self.configfile) as fh:
            return yaml.load(fh, Loader=yaml.FullLoader)
