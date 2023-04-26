Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    edge = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    for i in range(n):
        if len(edge[i]) != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    for i in range(M):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        if u == 1 and v == N:
            continue
        if u != i + 1 or v != i + 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    for i in range(m):
        u, v = map(int, input().split())
        if abs(u - v) >= 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    for _ in range(m):
        u, v = map(int, input().split())
        if abs(u - v) != 1:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    for i in range(M):
        u, v = map(int, input().split())
        if u > N or v > N:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if N == M + 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    if n == m:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print('No')
        return
    d = [0 for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        d[u - 1] += 1
        d[v - 1] += 1
    for i in range(n):
        if d[i] != 1:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    N,M = map(int, input().split())
    if M != N-1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return

    # 連結成分ごとに独立に考える
    # 連結成分の数を調べる
    # 連結成分の数が1つでなければNo
    # 連結成分の数が1つならば、パスグラフか判定する
    # 連結成分の数が1つならば、パスグラフか判定する
    # その連結成分の頂点の数がNならばYes
    # その連結成分の頂点の数がNでなければNo

    # 連結成分の数を調べる
    # 連結成分の数が1つでなければNo
    # 連結成分の数が1つならば、パスグラフか判定する

    # 連結成分の数を調べる
    # 連結成分の数が1つでなければNo
    # 連結成分の数が1つならば、パスグラフか判定する

    # 連結成分の数を調べる
    # 連結成分の数が1つでなければNo
    # 連結成分の数が1つならば、パスグラフか判定する

    # 連結成分の数を調べる
    # 連結成分の数が1つでなければNo
    # 連結成分の数が1つならば、パスグラフか判定する

    # 連結成分の数を調べる
    # 連結成分の数が1つでなければNo
    # 連結成分の数が1つ
