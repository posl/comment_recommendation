Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    return N, Q, A, X

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    b = [0] * (n + 1)
    for i in range(n):
        b[i] += a[i]
        b[i + 1] -= a[i]
    for i in range(n):
        b[i + 1] += b[i]
    for i in range(q):
        print(x[i] * n + b[n] - b[0])

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        ans = 0
        left = 0
        right = n - 1
        while left < right:
            if a[left] < x[i]:
                left += 1
            if a[right] > x[i]:
                right -= 1
            if a[left] >= x[i] and a[right] <= x[i]:
                break
        ans += min(abs(a[left] - x[i]), abs(a[right] - x[i]))
        ans += abs(a[left] - a[right])
        print(ans)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        i = 0
        j = N - 1
        while i < j:
            if A[i] < x:
                i += 1
            else:
                j -= 1
        if A[i] < x:
            print(2 * (x - A[i]) + N)
        else:
            print(N)

=======
Suggestion 5

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    s = sum(a)
    for i in range(q):
        print(s + x[i])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    A.sort()
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]
    for i in range(Q):
        left = 0
        right = N-1
        while left < right:
            mid = (left + right) // 2
            if A[mid] >= X[i]:
                right = mid
            else:
                left = mid + 1
        print(N* X[i] - s[left] - (N-left) * X[i])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    A.sort()
    A.append(0)
    A.append(10**9)

    for x in X:
        s = 0
        t = 0
        for i in range(N+1):
            if A[i] <= x:
                s += A[i]
            else:
                t += A[i]
        print(t-s)

main()

=======
Suggestion 8

def main():
    # input
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    # compute
    s = sum(a)
    for i in range(q):
        print(s + x[i] * n)

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]

    A.sort()
    A.append(0)
    A.append(10**9)
    A.sort()

    ans = 0
    for i in range(1, N+2):
        ans += (A[i]-A[i-1]) * (i-1) * (N-i+1)

    for x in X:
        print(ans + (x-A[0])*(N+1))

=======
Suggestion 10

def solve(n,q,a,x):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - x
    b.sort()
    s = sum(b)
    res = 0
    for i in range(n):
        if b[i] > 0:
            break
        res += -b[i]
    for i in range(n-1,-1,-1):
        if b[i] < 0:
            break
        res += b[i]
    return res

n,q = map(int,input().split())
a = list(map(int,input().split()))
x = [0] * q
for i in range(q):
    x[i] = int(input())
for i in range(q):
    print(solve(n,q,a,x[i]))
