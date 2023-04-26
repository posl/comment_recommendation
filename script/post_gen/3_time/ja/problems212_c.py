Synthesizing 10/10 solutions (Duplicates hidden)

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
    ans = float("inf")
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

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
    a = 0
    b = 0
    ans = 10**9
    while a < N and b < M:
        ans = min(ans, abs(A[a] - B[b]))
        if A[a] < B[b]:
            a += 1
        else:
            b += 1
    print(ans)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(ans,abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    ans = 10**9
    for a in A:
        l = 0
        r = M
        while r - l > 1:
            m = (l + r) // 2
            if B[m] <= a:
                l = m
            else:
                r = m
        ans = min(ans, abs(a - B[l]))
        if r < M:
            ans = min(ans, abs(a - B[r]))
    print(ans)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
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
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for i in range(N):
        idx = bisect_left(B, A[i])
        if idx == M:
            ans = min(ans, abs(A[i]-B[idx-1]))
        elif idx == 0:
            ans = min(ans, abs(A[i]-B[idx]))
        else:
            ans = min(ans, abs(A[i]-B[idx]), abs(A[i]-B[idx-1]))
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #ソート
    A.sort()
    B.sort()
    #初期化
    i = 0
    j = 0
    ans = 10**9
    #A,Bの要素を比較
    while i < N and j < M:
        ans = min(ans, abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    #出力
    print(ans)

=======
Suggestion 9

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    #Aを昇順にソート
    A.sort()
    
    #Bを昇順にソート
    B.sort()
    
    #Aの各要素とBの各要素の差を計算する
    #差の絶対値の最小値を出力する
    print(min([abs(a - b) for a in A for b in B]))
