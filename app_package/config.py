import os

base_dir=os.path.abspath(os.path.dirname(__file__))
class Config(object):
    MONGO_URI="mongodb://localhost:27017/datadb"
    