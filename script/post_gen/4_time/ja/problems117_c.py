Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort()
    ans = sum(diff[:m-n])
    print(ans)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort()
    ans = 0
    for i in range(m-n):
        ans += diff[i]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        exit()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1] - X[i])
    diff.sort()
    print(sum(diff[:M-N]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        exit()
    d = []
    for i in range(M-1):
        d.append(X[i+1] - X[i])
    d.sort(reverse=True)
    print(sum(d[N-1:]))

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort(reverse=True)
    print(sum(diff[n-1:]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))

    X.sort()

    if N >= M:
        print(0)
        exit()

    dist = [0] * (M - 1)
    for i in range(M - 1):
        dist[i] = X[i + 1] - X[i]

    dist.sort()
    print(sum(dist[:M - N]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(0)
        return
    ans = 0
    for i in range(m-1):
        ans += x[i+1] - x[i]
    ans -= (x[-1] - x[0])
    ans += min(x[0], x[-1])
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    a = [0] * (m - 1)
    for i in range(m - 1):
        a[i] = x[i + 1] - x[i]
    a.sort()
    print(sum(a[:m - n]))

=======
Suggestion 9

def main():
    # データ入力
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    # 座標の重複を削除してソートし、隣り合う座標の差を計算
    x = sorted(list(set(x)))
    d = [x[i+1] - x[i] for i in range(len(x)-1)]

    # 差の大きい順に並び替えて、前から n-1 個の差を足し合わせる
    d.sort(reverse=True)
    print(sum(d[n-1:]))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    # print(x)
    if n >= m:
        print(0)
        return
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort()
    # print(diff)
    print(sum(diff[:m-n]))
