from itertools import count
import requests as requests
from bs4 import BeautifulSoup
import pandas as pd


def bbqStore():
    bbqList = []

    for page in count(start=1):

        url = "http://changup.bbq.co.kr/findstore/findstore_ajax.asp?page=%s" % page

        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        trs = tbody.find_all("tr")

        if len(trs) <= 1:
            break

        for i, tr in enumerate(trs):
            if i != 0:
                str_list = list(tr.strings)

                name = str_list[1]
                tel = str_list[5]
                add = str_list[3]
                print(name, tel, add)
                bbqList.append([name, tel, add])
    table = pd.DataFrame(bbqList, columns=["name", "tel", "add"])
    table.to_csv("/Users/huxx_j/Downloads/ex/webdata/bbq_table.csv", encoding="utf-8-sig", mode='w', index=True)
    return bbqList


print(bbqStore())
