def main():
    N = int(input())
    A = list(map(int, input().split()))
    #Aの各要素の出現回数をカウント
    cnt = [0 for i in range(200001)]
    for i in range(N):
        cnt[A[i]] += 1
    #Aの各要素の出現回数を奇数のみにする
    for i in range(200001):
        cnt[i] %= 2
    #Aの各要素の出現回数の奇数の数をカウント
    odd = 0
    for i in range(200001):
        if cnt[i] == 1:
            odd += 1
    #Aの各要素の出現回数の奇数の数が0か1のとき、Aを回文にするのに必要な操作回数は0
    #それ以外のとき、Aを回文にするのに必要な操作回数は、Aの要素の出現回数の奇数の数-1
    if odd == 0 or odd == 1:
        print(0)
    else:
        print(odd-1)
