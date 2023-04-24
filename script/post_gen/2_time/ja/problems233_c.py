Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 3

def main():
    import sys
    from math import gcd
    input = sys.stdin.readline
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    A = [L[i][1:] for i in range(N)]
    G = [gcd(A[i][j], A[i][j+1]) for i in range(N) for j in range(L[i][0]-1)]
    for i in range(N):
        for j in range(L[i][0]):
            G.append(gcd(X, A[i][j]))
    G = list(set(G))
    ans = 0
    for i in range(len(G)):
        cnt = 0
        for j in range(N):
            for k in range(L[j][0]):
                if A[j][k] % G[i] == 0:
                    cnt += 1
        if cnt == N * L[0][0]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    #入力
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))

    #処理
    ans = 0
    for i in range(N):
        for j in range(1, L[i][0]+1):
            if X % L[i][j] == 0:
                ans += 1

    #出力
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    #print(N, X)
    #prin

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    #N個の袋の中身をリストに格納
    A = [list(map(int, input().split())) for _ in range(N)]
    #袋の中身を一つずつ取り出す
    for a in A:
        #袋の中身の個数を取得
        L = a.pop(0)
        #袋の中身の数を格納
        a = a
    #袋の中身を全て掛け合わせる
    #全ての袋の中身を掛け合わせた結果を格納するリスト
    A = []
    #袋の中身の個数を格納するリスト
    L = []
    #袋の中身を全て掛け合わせる
    for a in A:
        #袋の中身の個数を取得
        l = a.pop(0)
        #袋の中身の数を格納
        a = a
        #袋の中身の個数を格納
        L.append(l)
        #袋の中身を全て掛け合わせる
        for i in range(0, l):
            for j in range(i + 1, l):
                #袋の中身を全て掛け合わせた結果を格納
                A.append(a[i] * a[j])
    #袋の中身を全て掛け合わせた結果をソート
    A.sort()
    #袋の中身の個数をソート
    L.sort()
    #袋の中身を全て掛け合わせた結果の個数を格納
    l = len(A)
    #袋の中身を全て掛け合わせた結果の個数を格納
    L = len(L)
    #袋の中身を全て掛け合わせた結果の個数を格納

=======
Suggestion 7

def main():
    #データ入力
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    #Xの素因数分解
    X_list = prime_factorize(X)

    #Aの素因数分解
    A_list = []
    for i in range(N):
        A_list.append([])
        for j in range(1, A[i][0]+1):
            A_list[i].append(prime_factorize(A[i][j]))

    #Aの素因数分解のリストを1つのリストにまとめる
    A_list_sum = []
    for i in range(N):
        A_list_sum += A_list[i]

    #Xの素因数分解をAの素因数分解のリストにあるかどうかでカウントする
    count = 0
    for i in range(len(X_list)):
        if X_list[i] in A_list_sum:
            count += 1

    #Xの素因数分解の数と一致したらOK
    if count == len(X_list):
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(N, X)
    #print(A)
    #N=2, X=40
    #A=[[3, 1, 8, 4], [2, 10, 5]]
    #N=3, X=200
    #A=[[3, 10, 10, 10], [3, 10, 10, 10], [5, 2, 2, 2, 2, 2]]
    #N=3, X=1000000000000000000
    #A=[[2, 1000000000, 1000000000], [2, 1000000000, 1000000000], [2, 1000000000, 1000000000]]
    ans = 0
    #for i in r

=======
Suggestion 9

def main():
    #入力
    N, X = map(int, input().split())
    #N 個の袋の情報を入れるリスト
    bag = []
    #N 個の袋の情報を入力
    for i in range(N):
        bag.append(list(map(int, input().split())))
    #袋 i の j 番目のボールに書かれた数の総積が X になる取り出し方の個数
    ans = 0
    #袋 i の j 番目のボールを選ぶか選ばないかの全探索
    for i in range(2 ** N):
        #袋 i の j 番目のボールを選ぶか選ばないかのフラグ
        flag = [0] * N
        #袋 i の j 番目のボールを選ぶか選ばないかのフラグの設定
        for j in range(N):
            if (i >> j) & 1:
                flag[j] = 1
        #袋 i の j 番目のボールに書かれた数の総積
        mul = 1
        #袋 i の j 番目のボールに書かれた数の総積の計算
        for j in range(N):
            if flag[j] == 1:
                mul *= bag[j][1 + flag[j]]
        #袋 i の j 番目のボールに書かれた数の総積が X になる取り出し方の個数の計算
        if mul == X:
            ans += 1
    #出力
    print(ans)
