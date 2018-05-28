import requests
from bs4 import BeautifulSoup


def naver_card():
    card_id_list = []
    page = 3
    url = "https://card.search.naver.com/" \
          "?query=&where=service&start=&display=&sort=#%7B%22benfIdList%22%3A%22%22%2C%22" \
          "tagIdList%22%3A%22%22%2C%22isMobileCard%22%3A0%2C%22mrcIdList%22%3A%22%22%2C%22" \
          "cardCoIdList%22%3A%22%22%2C%22brandIdList%22%3A%22%22%2C%22cardType%22%3A%22%22%2C%22" \
          "annualFeeRangeIdList%22%3A%22%22%2C%22recordCondRangeIdList%22%3A%22%22%2C%22order%22%3A%22" \
          "pop%22%2C%22oe%22%3A%22json%22%2C%22where%22%3A%22service%22%2C%22anq%22%3A0%2C%22" \
          "query%22%3A%22%22%2C%22ssc%22%3A%22%22%2C%22affiliateBenefitType%22%3A%22%22%2C%22" \
          "start%22%3A%" \
          "2231" \
          "%22%2C%22display%22%3A%2210%22%2C%22so%22%3A%22%22%7D"

    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    ul_tag = soup.find("ul", {"class", "rst_lst"})
    label_tags = ul_tag.find_all("label", {"class": "checkbox-mark"})

    for label_tag in label_tags:
        id = label_tag.get("data_code")

        card_id_list.append(id)

    return card_id_list



print(naver_card())


