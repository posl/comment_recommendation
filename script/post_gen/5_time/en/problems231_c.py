Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - (len(a) - bisect.bisect_left(a, x[i])))

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        i = bisect.bisect_left(A, x)
        print(N - i)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        l = 0
        r = N-1
        while l < r:
            m = (l+r)//2
            if A[m] >= x:
                r = m
            else:
                l = m+1
        if A[l] >= x:
            print(N-l)
        else:
            print(0)

main()

=======
Suggestion 4

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
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(q):
        x = int(input())
        min = 0
        max = n
        while min < max:
            mid = (min + max) // 2
            if a[mid] < x:
                min = mid + 1
            else:
                max = mid
        print(n - min)

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    X = []
    for i in range(Q):
        X.append(int(input()))
    #print(N,Q,A,X)
    for i in range(Q):
        for j in range(N):
            if X[i] <= A[j]:
                print(N-j)
                break

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    X = [int(input()) for _ in range(Q)]
    X.sort()

    for x in X:
        left = 0
        right = N - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < x:
                left = mid + 1
            else:
                right = mid
        if A[left] < x:
            print(N)
        else:
            print(left)

=======
Suggestion 8

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for i in range(Q)]
    A.sort()
    A.append(10**10)
    for x in X:
        for i in range(N):
            if A[i] >= x:
                print(N-i)
                break

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort()

    for i in range(Q):
        x = int(input())
        idx = bisect.bisect_left(H, x)
        print(N - idx)

=======
Suggestion 10

def main():
    # Get input
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    # Get output
    ans = []
    for i in range(q):
        ans.append(len(list(filter(lambda y: y >= x[i], a))))

    # Print output
    for i in range(q):
        print(ans[i])
