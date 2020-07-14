import pdb
import sys
from scripts.adpter import Adpter
import pprint
import logging


if __name__ == '__main__':
    # url = "https://cws.gm.com/vs-cws/vehshop/v2/vehicles?conditions=New&makes=GMC&locale=en_US&models=Terrain&years=2020&radius=250&postalCode=89101&pageSize=24&sortby=bestMatch:desc,distance:asc,netPrice:asc&includeNearMatches=true&customerType=GC&requesterType=TIER_1_VSR&trims=Denali&netPrice=0:999999"
    logging.addLevelName(logging.DEBUG, 'INFO')
    logging.info("scrapping started")
    adpter = Adpter({'url':"http://jkmitchell.app.dealerslinkclassifieds.com/web_display/condition/New/", 'response':"html"})
    # adpter = Adpter({'url':"http://AFJKBJSVJDbkjsdvb vkasbjkvbjkvbskj vjkasbkjbvsfs", 'response':"html"})
    
    list_of_data = adpter.process_target()
    
    # pprint.pprint(list_of_data[0])
    
    # adpter.add_data_to_es(list_of_data)
    
    
	# print(f"response of bulk_heper is:{resp}")