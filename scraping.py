import requests
import random
from bs4 import BeautifulSoup as bs

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"class": "table table-striped table-bordered"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    # print(proxies)
    return proxies

proxies=get_free_proxies()


# txt=page.text
# status=page.status_code
# print(txt,status)

# # Extract title
# page_title=soup.title.text

# # Extract body
# page_body=soup.body

# # Extract title
# page_head=soup.head

# print(type(page_title),type(page_head),type(page_body))


random_proxy=random.choices(proxies)
print("Request #%d")

try:
    # url = 'https://www.google.com/'
    url = 'https://www.boatid.com/strike-king/pro-model-3xd-crank-7-16-oz-powder-blue-back-chartreuse-hard-bait-mpn-hc3xd-561.html'

    response = requests.get(url,proxies={'http': f"http://{random_proxy}"})
    # print(response.text)
    print(random_proxy)
    print(response.status_code)

    page = requests.get('https://www.boatid.com/strike-king/pro-model-3xd-crank-7-16-oz-powder-blue-back-chartreuse-hard-bait-mpn-hc3xd-561.html')
    soup = bs(page.content,'html.parser')

    print('-------------------h1 tags-------------')
    all_h1_tags=[]
    for element in soup.select('h1'):
        all_h1_tags.append(element.text)
    print(all_h1_tags)

    print('-------------------product-------------')
    product_title = soup.find('div', attrs={'div', 'body'}, class_="prod-offer-title")
    product_name = soup.find("div", class_="prod-offer-content")
    # content=product_name.find_all('a')
    print(product_title,product_name)

except:
    #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
    #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
    print("Skipping. Connnection error")

