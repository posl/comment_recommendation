def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
A, B, K = map(int, input().split())
# 1から100までの整数を格納するリスト
list = []
# 1から100までの整数をリストに格納する
for i in range(1, 101):
    list.append(i)
# 降順にソートする
list.sort(reverse=True)
# 答えを格納する変数
ans = 0
# 入力されたAとBの最大公約数を求める
gcd = gcd(A, B)
# 最大公約数であまりが0となるものをリストから削除する
for i in range(len(list)):
    if list[i] % gcd == 0:
        list[i] = 0
# 降順にソートする
list.sort(reverse=True)
# 0を削除する
while 0 in list:
    list.remove(0)
# K番目を求める
ans = list[K - 1]
print(ans)

if __name__ == '__main__':
    gcd()