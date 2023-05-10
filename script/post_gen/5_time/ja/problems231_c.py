Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    #処理
    A.sort()
    ans = [0] * Q
    for i in range(Q):
        ans[i] = N - (len(A) - bisect.bisect_left(A, X[i]))

    #出力
    for i in range(Q):
        print(ans[i])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        print(N - bisect.bisect_left(A, x))
    return

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        cnt = 0
        for a in A:
            if a >= x:
                cnt += 1
        print(cnt)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        l = 0
        r = N-1
        while r-l>1:
            m = (l+r)//2
            if A[m] >= x:
                r = m
            else:
                l = m
        if A[l] >= x:
            print(N-l)
        else:
            print(N-r)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    A.sort()
    for i in range(Q):
        x = X[i]
        l = 0
        r = N - 1
        while r - l > 1:
            m = (l + r) // 2
            if A[m] >= x:
                r = m
            else:
                l = m
        if A[l] >= x:
            print(N - l)
        elif A[r] >= x:
            print(N - r)
        else:
            print(0)

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * q
    for i in range(q):
        x[i] = int(input())
    a.sort()
    for i in range(q):
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if a[mid] < x[i]:
                left = mid + 1
            else:
                right = mid
        if a[left] < x[i]:
            print(n - left)
        else:
            print(n - left - 1)

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        idx = bisect.bisect_left(a, x)
        print(n-idx)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        i = 0
        j = N
        while j - i > 1:
            k = (i + j) // 2
            if A[k] >= x:
                j = k
            else:
                i = k
        print(N - j)

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        ans = 0
        ans = n - bisect.bisect_left(a, x)
        print(ans)

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))
