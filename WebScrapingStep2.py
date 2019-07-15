import requests
from bs4 import BeautifulSoup
import time
import scrapingfunction

res = requests.get("https://book.impress.co.jp/booklist");
status = res.status_code

print(status)

html_doc = res.text
# ポイント：HTML取得結果。150時まで
# print(html_doc[:150])

# オブジェクト生成
soup = BeautifulSoup(html_doc , 'html.parser')

# find / findAllで取り出す
# 書籍リストの部分、Aタグの部分
div_book_detail = soup.find('div', class_ = 'block-book-list-body')
book_urls = []

tags = div_book_detail.find_all('a')
for tag in tags:
    # 重複除外
    if tag['href'] not in book_urls:
        print('スクレイピング中' , tag['href'])
        scrapingfunction.get_book_info(tag['href'])
        # 1秒かえる。負荷かけないように
        time.sleep(1)

# ポイント：指定した要素を取り出す
print(book_urls)
