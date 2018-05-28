import time
from itertools import count

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


def goobneStore():
    goobneStoreList = []
    wd = webdriver.Chrome('/Users/huxx_j/Downloads/ex/chromedriver')
    wd.get('http://goobne.co.kr/store/search_store.jsp')

    for page in count(start=1):
        wd.execute_script('store.getList(%s)' % page)
        time.sleep(1)
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tbody_tag = soup.find('tbody', {'id': 'store_list'})
        tr_tags = tbody_tag.find_all('tr')

        if tr_tags[0].get("class") is None:
            break
        for tr_tag in tr_tags:

            stringList = list(tr_tag.strings)
            print(stringList)
            name = stringList[1]
            tel = stringList[3]
            add = stringList[5] if stringList[3] == ' ' else stringList[6]

            goobneStoreList.append([name, tel, add])

    table = pd.DataFrame(goobneStoreList, columns=["name", "tel", "add"])
    table.to_csv("/Users/huxx_j/Downloads/ex/webdata/goobne_table.csv", encoding="utf-8-sig", mode='w', index=True)
    return goobneStoreList


result = goobneStore()
print(result)
