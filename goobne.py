import time

from bs4 import BeautifulSoup
from selenium import webdriver


def goobne():
    wd = webdriver.Chrome("/Users/huxx_j/Downloads/ex/chromedriver")
    wd.get("http://goobne.co.kr/store/search_store.jsp")
    page = 1
    wd.execute_script("store.getList(%s)" % page)
    html = wd.page_source
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(2)
    tag = soup.find("tbody", {"id": "store_list"})
    tags = tag.find_all("tr")
    print(tags)


goobne()
