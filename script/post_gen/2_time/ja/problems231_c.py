Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_right(A, x[i]))

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(N - bisect.bisect_left(A, x))

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for i in range(Q)]
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_left(A, x[i]))

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    A.sort()
    for x in X:
        print(N - A[::-1].index(x) - 1)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in x:
        print(N - bisect.bisect_right(A, i))

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in x:
        print(n - bisect.bisect_right(a, i))

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    for x in X:
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if B[m] >= x:
                r = m
            else:
                l = m
        print(N - l)

=======
Suggestion 8

def main():
    #入力
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for _ in range(Q)]

    #Aを降順にソート
    A.sort(reverse=True)

    #Aの累積和を計算
    A_sum = [0] * (N+1)
    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]

    #xを昇順にソート
    x.sort()

    #xの各要素に対して、Aの累積和で二分探索
    for i in range(Q):
        ok = N
        ng = 0
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if A_sum[mid] >= x[i]:
                ok = mid
            else:
                ng = mid
        print(N-ok)

=======
Suggestion 9

def main():
    #入力
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    #身長の降順にソート
    A.sort(reverse=True)
    #print(A)
    #print(X)
    #出力
    for i in range(Q):
        print(binary_search(A,X[i]))
