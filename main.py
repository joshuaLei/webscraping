import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://www.physicsandmathstutor.com/past-papers/a-level-physics/edexcel-unit-1/"

folder_location = r'PHYU1'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")
for link in soup.select("a[href$='.pdf']"):
    print(link)

    if 'MS' in link['href']:
        if not os.path.exists(folder_location+"/MS"): os.mkdir(folder_location+"/MS")
        filename = os.path.join(folder_location+"/MS",link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
    elif 'QP' in link['href']:
        if not os.path.exists(folder_location+"/QP"): os.mkdir(folder_location+"/QP")
        filename = os.path.join(folder_location + "/QP", link['href'].split('/')[-1])
        with open(filename, 'wb') as g:
            g.write(requests.get(urljoin(url, link['href'])).content)
    else:
        if not os.path.exists(folder_location+"/others"): os.mkdir(folder_location+"/others")
        filename = os.path.join(folder_location + "/others", link['href'].split('/')[-1])
        with open(filename, 'wb') as h:
            h.write(requests.get(urljoin(url, link['href'])).content)