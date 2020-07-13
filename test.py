import requests
from bs4 import BeautifulSoup
import pdb
import pprint


url = "http://jkmitchell.app.dealerslinkclassifieds.com/web_display/condition/New"
print(f"url is : {url}")
soup = BeautifulSoup((requests.get(url).content), 'html.parser')
data_arr = []
sections = (soup.find_all("div", class_= "vehicle-padding"))[0].find_all('section')

for _listing in sections:  
    obj = {}
    obj['title'] = (_listing.find('h2').get_text())
    obj['price'] = (_listing.find('h2',class_= 'price').text)
    obj['exterior'] = (_listing.div.tbody).find('td' , text = 'Exterior:').find_next_siblings()[0].text
    obj['interior'] = (_listing.div.tbody).find('td' , text = 'Interior:').find_next_siblings()[0].text
    obj['condition'] = (_listing.div.tbody).find('td' , text = 'Condition:').find_next_siblings()[0].text
    obj['odometer'] = int((_listing.div.tbody).find('td' , text = 'Odometer:').find_next_siblings()[0].text)
    obj['link'] = url+_listing.find('a', href=True)['href']
    
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
pdb.set_trace()    

