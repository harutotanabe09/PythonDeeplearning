from sklearn import datasets
from matplotlib import pyplot

# scikit learningの学習用データ
x,y = datasets.load_digits(return_X_y = True)

#　ポイント：特徴行列を確認
# print(x)
# print(x.shape)

# print(y)
# print(y.shape)

# ポイント：１次元のndarray
x0 = x[0]
#print(x0)
#print(x0.shape)

# ポイント：２次元のndarray。8×8で表示
x0_square = x0.reshape(8,8)
#print(x0_square)
#print(x0_square.shape)

fig, ax = pyplot.subplots()
ax.imshow(x0_square, cmap='binary')