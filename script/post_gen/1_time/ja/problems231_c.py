Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_left(A, x[i]))

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(N - bisect.bisect_right(A, x))

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]

    A.sort()

    for i in range(Q):
        left = -1
        right = N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] > x[i]:
                right = mid
            else:
                left = mid
        print(N - right)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    A.sort()

    for x in X:
        print(N - bisect.bisect_left(A, x))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]
    A.sort()
    for x in X:
        print(bisect.bisect_left(A, x))

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]

    A.sort()
    for i in x:
        print(N - bisect.bisect_right(A, i))

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    for i in range(q):
        print(bisect.bisect_left(a, x[i]))

=======
Suggestion 8

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for i in range(Q)]
    A.sort()
    for i in range(Q):
        l,r = 0,N
        while r-l > 1:
            m = (r+l)//2
            if A[m] > x[i]:
                r = m
            else:
                l = m
        print(N-r)

=======
Suggestion 9

def main():
    # 標準入力の値を取得
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]

    # 二分探索を行うため、Aをソート
    A.sort()

    # xの値について、Aにおけるx以上の値の数を出力
    for i in range(Q):
        # 二分探索
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if A[mid] >= x[i]:
                right = mid
            else:
                left = mid + 1
        print(N - left)

=======
Suggestion 10

def main():
    #入力
    #N,Q = map(int, input().split())
    #A = list(map(int, input().split()))
    #X = [int(input()) for _ in range(Q)]
    N,Q = 5,5
    A = [804289384, 846930887, 681692778, 714636916, 957747794]
    X = [424238336, 719885387, 649760493, 596516650, 189641422]
    
    #Aの要素をソート
    A.sort()
    
    #Xの要素を昇順にソート
    X.sort()
    
    #Aの要素を二分探索
    for x in X:
        print(bisect.bisect_left(A, x))
