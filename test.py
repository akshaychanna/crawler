import requests
from bs4 import BeautifulSoup
import pdb


url = "http://jkmitchell.app.dealerslinkclassifieds.com/web_display/condition/New"
print(f"url is : {url}")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
sample = []
headings = []
divs = soup.find_all("div", class_= "vehicle-padding")

for data in divs:
    sample.append(data.find_all('section'))

for _listing in sample[0]:  
    headings.append(_listing.find('h2',attrs={'title'}).get_text())
        
    
pdb.set_trace()    
    
    

