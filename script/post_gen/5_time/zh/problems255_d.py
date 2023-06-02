Synthesizing 10/10 solutions

=======
Suggestion 1

def problem255_d():
    pass

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    sum_a = sum(a)
    for i in range(q):
        print(sum_a + x[i] * n)

=======
Suggestion 3

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for i in range(q)]
    print(n,q)
    print(a)
    print(x)
    return 0

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for i in range(q)]

    a.sort()
    s = sum(a)
    for i in range(q):
        s += x[i]
        print(s)
        if s < 0:
            s = sum(a)
        else:
            s += x[i] * n

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort(reverse=True)
    X.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - X[i])
    print(ans)

=======
Suggestion 6

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    s = sum(a)
    for i in range(q):
        print(s + x[i] * n)
solve()

=======
Suggestion 7

def solve(n,q,a,x):
    a.sort()
    x.sort()
    total = sum(a)
    ans = []
    for i in range(q):
        cnt = 0
        for j in range(n):
            if a[j] < x[i]:
                cnt += x[i]-a[j]
        ans.append(total+cnt)
    return ans

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    sum = [0 for _ in range(n)]
    sum[0] = a[0]
    for i in range(1,n):
        sum[i] = sum[i-1] + a[i]
    for i in range(q):
        idx = 0
        ans = 0
        while idx < n and a[idx] < x[i]:
            ans += a[idx]
            idx += 1
        if idx == n:
            print(sum[n-1] + (x[i] - a[n-1]) * n)
        else:
            print(ans + (n-idx)*x[i])

=======
Suggestion 9

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    ans = []
    for i in range(Q):
        count = 0
        for j in range(N):
            if A[j] > X[i]:
                count += A[j] - X[i]
            else:
                count += X[i] - A[j]
        ans.append(count)
    for i in range(Q):
        print(ans[i])

=======
Suggestion 10

def solve(n, q, a, x):
    print(n, q)
    print(a)
    print(x)
    return
