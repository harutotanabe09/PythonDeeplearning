from janome.tokenizer import Tokenizer

# 形態素分析を使う
t = Tokenizer()
text = '東京でおいしいビール飲む'

# 解析結果を表示。単語ごと・品詞が表示される
# tokens = t.tokenize(text)

# わかち書きする。語区切りにする
tokens = t.tokenize(text, wakati=True)

for token in tokens:
    print(token)

