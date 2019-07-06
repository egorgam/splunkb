from app import log, spc, mng
import splunklib.client as client
import splunklib.results as results
import pymongo
import time

class DB():

    def __init__(self, collection):
        self.collection = collection
        self.connect()
        
    def connect(self):
        while True:
            try:
                self.col = pymongo.MongoClient(mng['host'], int(mng['port'])).splunk[self.collection]
                break
            except Exception:
                log.warn('[ERROR] Can`t connect to MongoDB')
            time.sleep(2)


class Splunk:

    def __init__(self):
        self.connect()
        
    def connect(self):
        while True:
            try:
                self.service = client.connect(host=spc['host'], port=spc['port'],
                                   username=spc['user'], password=spc['password'])

                self.results = results
                self.ns = client.namespace(sharing='user', owner='wall', app='splunkb_templates')

                break
            except Exception:
                log.warn('[ERROR] Can`t connect to Splunk')
                time.sleep(2)

