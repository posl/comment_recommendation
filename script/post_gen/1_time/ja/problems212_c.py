Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)
main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    i = j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**10
    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    ans = 10**9+1
    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0
    ans = 10**9 + 1
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(ans)

=======
Suggestion 8

def main():
    import sys
    readline = sys.stdin.readline
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    A.sort()
    B.sort()
    ans = 10**9
    a = 0
    b = 0
    while a < N and b < M:
        ans = min(ans, abs(A[a]-B[b]))
        if A[a] > B[b]:
            b += 1
        else:
            a += 1
    print(ans)

=======
Suggestion 9

def main():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 処理
    A.sort()
    B.sort()
    # 出力
    print(min([abs(A[i]-B[j]) for i in range(N) for j in range(M)]))

=======
Suggestion 10

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
