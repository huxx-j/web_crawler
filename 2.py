import json
import time
from collections import Counter
from itertools import count

import requests
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from selenium import webdriver


def naver_card_id():
    card_id_list = []
    for page in range(0, 32):
        wd = webdriver.Chrome('/Users/huxx_j/Downloads/ex/chromedriver')
        wd.get("https://card.search.naver.com/" \
               "?query=&where=service&start=&display=&sort=#%7B%22benfIdList%22%3A%22%22%2C%22" \
               "tagIdList%22%3A%22%22%2C%22isMobileCard%22%3A0%2C%22mrcIdList%22%3A%22%22%2C%22" \
               "cardCoIdList%22%3A%22%22%2C%22brandIdList%22%3A%22%22%2C%22cardType%22%3A%22%22%2C%22" \
               "annualFeeRangeIdList%22%3A%22%22%2C%22recordCondRangeIdList%22%3A%22%22%2C%22order%22%3A%22" \
               "pop%22%2C%22oe%22%3A%22json%22%2C%22where%22%3A%22service%22%2C%22anq%22%3A0%2C%22" \
               "query%22%3A%22%22%2C%22ssc%22%3A%22%22%2C%22affiliateBenefitType%22%3A%22%22%2C%22" \
               "start%22%3A%" \
               "22{0}1" \
               "%22%2C%22display%22%3A%2210%22%2C%22so%22%3A%22%22%7D".format(page))

        time.sleep(1)
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        ul_tag = soup.find("ul", {"class", "rst_lst"})
        label_tags = ul_tag.find_all("label", {"class": "checkbox-mark"})

        for label_tag in label_tags:
            id = label_tag.get("data_code")

            card_id_list.append(id)

    return card_id_list


# print(naver_card_id())

def naver_card_info():
    url = "https://card.search.naver.com/card.naver?singleCardId=20"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    div_tags = soup.find("div", {"class": "_detail_1 sum_one sum_one_v1 _tab_detail"})
    tr_tags = div_tags.find_all("tr")
    del tr_tags[0]
    t = list(tr_tags[1].strings)
    lists = []
    for temp in t:
        if temp == '\n':
            del temp
        else:
            lists.append(temp)

    twitter = Twitter()
    nouns = twitter.nouns(' '.join(lists))
    pos = twitter.pos(' '.join(lists))
    morph = twitter.morphs(' '.join(lists))
    phrases = twitter.phrases(' '.join(lists))

    count = Counter(nouns)
    print(lists)
    print(pos)
    print(morph)
    print(phrases)
    print(nouns)
    print(count)

    # with open("/Users/huxx_j/Downloads/ex/1530.txt", 'w', encoding='utf-8') as outfile:
    #     json_string = json.dumps(html, indent=4, sort_keys=True, ensure_ascii=False)
    #     outfile.write(json_string)



naver_card_info()

list = ['20', '1530', '5', '2326', '2355', '1408', '10', '223', '1322', '1465', '2337', '1246', '2325', '2225', '2226',
        '247', '592', '2368', '1221', '1653', '1772', '1927', '1623', '870', '2005', '1327', '1926', '2395', '2186',
        '1684', '593', '2207', '1617', '2378', '2412', '1451', '9', '2413', '1154', '1294', '2336', '1608', '2315',
        '248', '2332', '2313', '1773', '1570', '2105', '1965', '244', '2310', '1092', '1687', '1692', '1600', '1259',
        '1612', '2327', '1946', '2354', '1362', '116', '1715', '1656', '2415', '2353', '1655', '1202', '2417', '2416',
        '2307', '1768', '611', '1806', '2069', '1614', '1336', '1334', '990', '2146', '286', '2328', '590', '1807',
        '1865', '277', '930', '1361', '1695', '2145', '1195', '634', '2348', '1162', '1223', '1866', '1410', '1531',
        '1224', '1222', '1155', '289', '2344', '2206', '1571', '1452', '1472', '1203', '1889', '1615', '1400', '2343',
        '1716', '1601', '2085', '1573', '2205', '1360', '1339', '1314', '2345', '1262', '2071', '2377', '1321', '1885',
        '1696', '2339', '1444', '1443', '652', '1244', '2305', '290', '1925', '1689', '1153', '1888', '1170', '1384',
        '1654', '1329', '1157', '1769', '1621', '155', '38', '409', '1340', '1201', '1625', '1391', '1337', '1158',
        '1241', '2165', '2185', '1691', '1316', '1886', '93', '206', '1887', '1690', '1229', '1597', '1228', '1225',
        '1227', '1698', '614', '1577', '671', '1030', '612', '1552', '1596', '613', '1572', '1313', '2356', '1171',
        '2265', '637', '1616', '1242', '104', '653', '1373', '124', '98', '1929', '1699', '1928', '1160', '115', '160',
        '1290', '137', '2341', '1291', '2347', '2125', '1697', '1660', '2072', '1682', '621', '1151', '2065', '1867',
        '790', '2285', '2351', '111', '1238', '2334', '470', '1683', '112', '1945', '1645', '2349', '2333', '1868',
        '2330', '1681', '1591', '2346', '2350', '1611', '2338', '1317', '1845', '1456', '1460', '1618', '1455', '650',
        '2352', '1805', '1658', '2392', '450', '1166', '1665', '2331', '1649', '1461', '1312', '1870', '1657', '2314',
        '1659', '2066', '1308', '633', '1619', '1445', '1872', '1613', '1680', '1605', '2068', '1725', '1399', '1110',
        '512', '1620', '1397', '1402', '1363', '1404', '1409', '1130', '1403', '1150', '2388', '2316', '148', '1463',
        '2067', '133', '1693', '1967', '2312', '1686', '1700', '2394', '2311', '1694', '1707', '1010', '1706', '1328',
        '1396', '1705', '2309', '1648', '1311', '1432', '2393', '1701', '1745', '1428', '1430', '1466', '2306', '386',
        '1425', '1433', '1708', '1424']


