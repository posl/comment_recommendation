Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if a[m] >= x[i]:
                r = m-1
            else:
                l = m+1
        print(n-l)

main()

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        x = X[i]
        idx = bisect_left(A, x)
        print(N - idx)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    a.sort()

    for i in range(q):
        ans = n
        l = 0
        r = n - 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] < x[i]:
                l = m
            else:
                r = m
        if a[l] >= x[i]:
            ans -= 1
        if a[r] >= x[i]:
            ans -= 1
        print(ans)

=======
Suggestion 4

def countGreater(arr, n, k):
    l = 0
    r = n - 1
    leftGreater = n
    while (l <= r):
        m = int(l + (r - l) / 2)
        if (arr[m] >= k):
            leftGreater = m
            r = m - 1
        else:
            l = m + 1
    return (n - leftGreater)
 
# Driver program
n,q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(q):
    k = int(input())
    print(countGreater(arr, n, k))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        if x < A[0]:
            print(N)
        elif x > A[N-1]:
            print(0)
        else:
            # binary search
            left = 0
            right = N-1
            while left < right:
                mid = (left + right) // 2
                if A[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            print(N - left)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    A.sort()
    for x in X:
        pos = bisect.bisect_left(A, x)
        print(N - pos)

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    x = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(n - bisect.bisect_left(a, x[i]))
    print(*ans, sep='\n')

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        ans = n
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if a[mid] >= x[i]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        print(ans)

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        print(n - len([j for j in a if j < x]))

=======
Suggestion 10

def solve(N, Q, A, x):
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_left(A, x[i]))
