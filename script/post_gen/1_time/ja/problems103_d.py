Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    bridge = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        bridge[a] += 1
        bridge[b] += 1

    print(bridge.count(1))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    L = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        L[a-1] += 1
        L[b-1] += 1
    print(L.count(1))

=======
Suggestion 3

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    #print(N, M)
    #print(AB)
    #print(AB[0][1])
    #print(AB[1][1])
    #print(AB[2][1])
    #print(AB[3][1])
    #print(AB[4][1])
    #print(AB[5][1])
    #print(AB[6][1])
    #print(AB[7][1])
    #print(AB[8][1])
    #print(AB[9][1])
    #print(AB[10][1])
    ans = 0
    #print(AB)
    #print(AB[0][0])
    #print(AB[1][0])
    #print(AB[2][0])
    #print(AB[3][0])
    #print(AB[4][0])
    #print(AB[5][0])
    #print(AB[6][0])
    #print(AB[7][0])
    #print(AB[8][0])
    #print(AB[9][0])
    #print(AB[10][0])
    for i in range(M):
        #print(AB[i][0])
        #print(AB[i][1])
        if AB[i][0] == AB[i][1]:
            ans += 1
        elif AB[i][0] < AB[i][1]:
            AB[i][0] += 1
            #print(AB[i][0])
            #print(AB[i][1])
            #print(AB)
            #print(AB[0][0])
            #print(AB[1][0])
            #print(AB[2][0])
            #print(AB[3][0])
            #print(AB[4][0])
            #print(AB[5][0])
            #print(AB[6][0])
            #print(AB[7][0])
            #print(AB[8][0])
            #print(AB[9][0])
            #print(

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    i = 0
    while i < M:
        ans += 1
        j = i
        while j < M and AB[i][1] >= AB[j][0]:
            j += 1
        i = j
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = [0 for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        X[a-1] += 1
        X[b-1] += 1
    print(max(X))

=======
Suggestion 6

def main():
    #入力
    N, M = map(int, input().split())
    ab = []
    for _ in range(M):
        ab.append(list(map(int, input().split())))
    #print(N, M)
    #print(ab)
    #print(ab[0][0])

    #各島の連結成分を管理するリスト
    #各島は連結成分の番号で管理する
    #連結成分の番号は1から順に振られる
    #連結成分の番号が-1の場合は、その島は未連結
    #つまり、未連結の島同士は自由に橋を渡ることができる
    #連結成分の番号が0の場合は、その島は取り除かれている
    #つまり、取り除かれた島同士は橋を渡ることができない
    #連結成分の番号が1以上の場合は、その島は連結成分の番号に対応する島と連結
    #つまり、連結成分の番号に対応する島と連結成分の番号に対応する島との間は橋を渡ることができない
    #連結成分の番号が1以上の島は、連結成分の番号に対応する島と連結
    #つまり、連結成分の番号に対応する島との間は橋を渡ることができない
    #連結成分の番号が-1の島は、自由に橋を渡ることができる
    #つまり、連結成分の番号が-1の島同士は

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    ab.reverse()
    bridge = [1] * n
    for a, b in ab:
        bridge[a-1] = 0
        bridge[b-1] = 0
        if bridge[a-1] == 0 and bridge[b-1] == 0:
            bridge[b-1] = 1
    print(sum(bridge))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # 連結成分の個数
    cnt = N
    # 連結成分のリスト
    # 連結成分の番号は 1 から N まで
    # 連結成分の番号は 0 から N-1 まで
    # 連結成分の要素数は 1 以上
    # 連結成��

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges = list(reversed(edges))
    #print(edges)
    bridge = [0 for _ in range(n-1)]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a > b:
            a, b = b, a
        bridge[a-1] = 1
        if a != b-1:
            bridge[b-2] = 1
    print(sum(bridge))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 連結成分の数を管理するリスト
    # 0番目は使わない
    # i番目はi番目の島が属する連結成分の番号
    # 連結成分の番号は1から始まる
    # 0番目はダミー
    # 連結成分の番号を管理するリスト
    # 0番目はダミー
    # 連結成分の数を管理するリスト
    # 0番目はダミー
    # 連結成分の番号を管理するリスト
    # 0番目はダミー
    # 連結成分の数を管理するリスト
    # 0番目はダミー
    # 連結成分の番号を管理するリスト
    # 0番目はダミー
    # 連結成
