Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        ans = n
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] < x[i]:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        print(n-ans)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    A.sort()
    for i in range(Q):
        cnt = 0
        for j in range(N):
            if A[j] >= X[i]:
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
        if x < A[0]:
            print(N)
        elif x >= A[-1]:
            print(0)
        else:
            l = 0
            r = N-1
            while l+1 < r:
                m = (l+r)//2
                if A[m] >= x:
                    r = m
                else:
                    l = m
            print(N-r)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        ans = 0
        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] >= x:
                ans = N - mid
                right = mid - 1
            else:
                left = mid + 1
        print(ans)

=======
Suggestion 6

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        count = 0
        for j in range(n):
            if x <= a[j]:
                count += 1
        print(count)

=======
Suggestion 7

def solve():
    import sys
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        ans = n - bisect.bisect_left(a, x)
        print(ans)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        #print(x)
        #print(A)
        #print(N)
        #print(bisect.bisect_left(A, x))
        print(N - bisect.bisect_left(A, x))

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        #print(x)
        #print(A)
        #print(A.index(x))
        #print(A.count(x))
        print(N - A.index(x))

=======
Suggestion 10

def binary_search(array, target):
    """二分探索の実装

    Args:
        array (list): 検索対象の配列
        target (int): 検索する値

    Returns:
        int: 検索結果のインデックス
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
