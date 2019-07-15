import requests
from bs4 import BeautifulSoup


res = requests.get("https://book.impress.co.jp/books/1116101151");
status = res.status_code

print(status)

html_doc = res.text
# ポイント：HTML取得結果。150字数まで
# print(html_doc[:150])

# オブジェクト生成
soup = BeautifulSoup(html_doc , 'html.parser')

# find / findAllで取り出す
# find 配下の要素をまるごと取得
div_book_detail = soup.find('div', class_ = 'block-book-detail')

# ポイント：特定のは以下のみを取り出す
# print(div_book_detail)

# find 特定の要素のみ
book_title = div_book_detail.find('h2')

# ポイント：テキストのみ取り出す
# print(book_title.get_text())

# dt,dd タグの内容を配列に変換する
dl_book_data = div_book_detail('dl' , class_ = 'module-book-data')
book_data = {}

tags = div_book_detail.find_all(['dt','dd'])

for tag in tags:
    if tag.name == 'dt': 
        key = tag.get_text()
    if tag.name == 'dd':
        book_data[key] = tag.get_text().strip()

# ポイント：指定した要素を取り出す
print(book_data['発売日'])
