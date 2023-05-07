def main():
    #入力
    #数列の長さを入力
    n,m = map(int,input().split())
    #数列A
    A = list(map(int,input().split()))
    #数列B
    B = list(map(int,input().split()))
    #処理
    #数列Aの要素を昇順にソート
    A.sort()
    #数列Bの要素を昇順にソート
    B.sort()
    #数列Aの各要素に対し、数列Bの要素との差の絶対値を計算し、最小値を求める
    #それぞれの値をリストに格納
    list = []
    for i in range(n):
        for j in range(m):
            list.append(abs(A[i]-B[j]))
    #出力
    #最小値を出力
    print(min(list))
