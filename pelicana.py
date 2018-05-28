from itertools import count
import requests
from bs4 import BeautifulSoup


def pelicanaStore():
    pelicana_list = []

    # for page in count(start=1):
    for page in range(115, 120):
        url = "http://www.pelicana.co.kr/store/stroe_search.html?page=%s" % page
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", {"class": "table mt20"})
        tbody = table.find("tbody")
        tr = tbody.find_all("tr")

        for tr_tag in tr:
            store_data = list(tr_tag.strings)
            name = store_data[1]
            tel = store_data[5].strip()
            add = store_data[3]

            pelicana_list.append([name, tel, add])
    return pelicana_list


result = pelicanaStore()

print(result)
