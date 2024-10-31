from bllose.config.Config import bConfig
from bllose.config.Config import class_config
import json

@bConfig()
def insertConfigTest(config):
    print(json.dumps(config))


@class_config
class myClass():
    def __init__(self, config):
       print(json.dumps(config)) 

if __name__ == '__main__':
    myClass()