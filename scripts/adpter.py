from bs4 import BeautifulSoup
import requests
import pdb
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import logging

class Adpter(object):
    def __init__(self,hash):
        self.url = hash['url']
        self.response_type = hash['response']
        # self.es  = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
    

    def process_target(self):
        
        arr = []
        pdb.set_trace()
        print(type(self.response_type))
        if self.response_type == 'html':
            curl_data = requests.get(self.url)
            dom = BeautifulSoup(curl_data.content, 'html.parser')
            
        else:
            data = requests.get(self.url).json()
            listings_data = data["vehicles"]
        
            for _listing in listings_data:
                arr.append({
                    'vin' : _listing['vin'],
                    'condition' : _listing['condition'],
                    'intransit' : _listing['intransit'],
                    'exactMatch' : _listing['exactMatch'],
                    'year' : _listing['year'],
                    'make' : _listing['make'],
                    'model' : _listing['model']
                })    
            return arr
        
        return arr
        
           
    def add_data_to_es(self, bulk_data):
        resp = helpers.bulk(
			self.es,
			bulk_data,
			index = "gmc_index",
			doc_type = "_doc"
		)		 
            
    

