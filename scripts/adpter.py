from bs4 import BeautifulSoup
import requests
import pdb
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import logging
import pprint


class Adpter(object):
    def __init__(self,hash):
        self.url = hash['url']
        self.response_type = hash['response']
        self.es  = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
        # logging.basicConfig(format='%(asctime)s -%(message)s', level = logging.INFO)
    

    def process_target(self):
        data_arr = []
        logging.addLevelName(logging.DEBUG, 'DEBUG')
        print("started....")
        
        if self.response_type == 'html':
            try:
                r = requests.get(self.url, timeout=3)
                logging.info(r.status_code)
                soup = BeautifulSoup((r.content), 'html.parser')
                print(soup.status_code)
                sections = (soup.find_all("div", class_= "vehicle-padding"))[0].find_all('section')

                for _listing in sections:  
                    obj = {}
                    obj['title'] = _listing.find('h2').get_text()
                    obj['price'] = _listing.find('h2',class_= 'price').text
                    obj['exterior'] = (_listing.div.tbody).find('td' , text = 'Exterior:').find_next_siblings()[0].text
                    obj['interior'] = (_listing.div.tbody).find('td' , text = 'Interior:').find_next_siblings()[0].text
                    obj['condition'] = (_listing.div.tbody).find('td' , text = 'Condition:').find_next_siblings()[0].text
                    obj['odometer'] = int((_listing.div.tbody).find('td' , text = 'Odometer:').find_next_siblings()[0].text)
                    obj['link'] = self.url+_listing.find('a').get('href')
                    data_arr.append(obj)
                    
                for i in data_arr:
                    dom = BeautifulSoup((requests.get(i['link']).content),'html.parser')
                    division = dom.find('div', class_ = 'details_holder')
                    
                    i['milage'] = int((division.ul.find('span',text = 'Mileage')).find_next_siblings()[0].text)
                    i['engine'] = (division.ul.find('span',text = 'Engine')).find_next_siblings()[0].text
                    i['transmission'] = (division.ul.find('span',text = 'Transmission')).find_next_siblings()[0].text
                    i['exterior color'] = (division.ul.find('span',text = 'Exterior Color')).find_next_siblings()[0].text
                    i['interiro color'] = (division.ul.find('span',text = 'Interior Color')).find_next_siblings()[0].text  
                    break
                
                print("loading into file")
                with open('res.json','w') as data:
                    json.dump(data_arr,data)
                
            except requests.exceptions.MissingSchema as e:
                print("given url is invalid")   
                
            except:
                print("something went wrong")
            
            
                
        else:
            data = requests.get(self.url).json()
            listings_data = data["vehicles"]
        
            for _listing in listings_data:
                data_arr.append({
                    'vin' : _listing['vin'],
                    'condition' : _listing['condition'],
                    'intransit' : _listing['intransit'],
                    'exactMatch' : _listing['exactMatch'],
                    'year' : _listing['year'],
                    'make' : _listing['make'],
                    'model' : _listing['model']
                })    
            # return data_arr
        
        
            
        return data_arr
           
        # def add_data_to_es(self, bulk_data):
        #     resp = helpers.bulk(
        # 		self.es,
        # 		bulk_data,
        # 		index = "gmc_index",
        # 		doc_type = "_doc"
        # 	)		 
            
    

