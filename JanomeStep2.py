from janome.tokenizer import Tokenizer
from math import log

# 形態素分析を使う
t = Tokenizer()
sentenses = ['東京でおいしいビール飲む' , 'コーヒー飲む' , '東京でうまいビール買う', '東京に帰る']

words_list = []

for sentense in sentenses:
    # わかち書きする。語区切りにする
    words_list.append(t.tokenize(sentense, wakati=True))

# それぞれのセンテンスを単語区切り
print(words_list)

unique_words = []

# それぞれのセンテンスの単語を表示
for words in words_list:
    for word in words:
        # 重複する値を除外
        if word not in unique_words:
            unique_words.append(word)

print(unique_words)

# Bag of Wordsのデータ作成
bow_list = []
for words in words_list:
    bag_of_words = []
    for unique_word in unique_words:
        # 一意な数をカウントする
        num = words.count(unique_word)
        bag_of_words.append(num)
    bow_list.append(bag_of_words)

# 単語の重み付け
print(bow_list)

# IDF ある単語がどのくらい出現しているか
# IDF計算 log 全体の文章 / 単語の出現回数  
num_of_sentenses = len(sentenses)
idf = []
for i in range(len(unique_words)):
    count = 0
    for bow in bow_list:
        if bow[i] > 0:
             count += 1
    idf.append(log ( (num_of_sentenses + 1) / (count + 1)))

print(idf)

# TF-IDF １つの文章でどのくらい出現したか

# 1センテンスを例にする
bow = bow_list[1]
num_of_words = sum(bow)
tfidf = []
for i , value in enumerate(bow):
    # TFを計算
    tf = value / num_of_words
    tfidf.append(tf * (idf[i] + 1 ))

print(tfidf)






