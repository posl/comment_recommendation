Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    if N == 1:
        print(1)
        return
    if A[0] != 1:
        A.insert(0, 0)
    if A[-1] != N:
        A.append(N+1)
    k = 0
    for i in range(1, len(A)):
        if A[i] - A[i-1] - 1 > k:
            k = A[i] - A[i-1] - 1
    ans = 0
    for i in range(1, len(A)):
        if A[i] - A[i-1] - 1 == k:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 > 0:
            B.append(A[i+1] - A[i] - 1)
    B.sort()
    if B[0] == 0:
        print(0)
        exit()
    k = B[0]
    ans = 0
    for i in range(len(B)):
        ans += (B[i] + k - 1) // k
    print(ans)

=======
Suggestion 4

def problem185_d():
    pass

=======
Suggestion 5

def solve(n, m, a):
    a.sort()
    if m == 0:
        return 1
    if m == n:
        return 0
    if m == 1:
        return n - 1
    d = []
    for i in range(m - 1):
        d.append(a[i + 1] - a[i] - 1)
    d.sort()
    return n - 1 - sum(d[-(m - 1):])

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    if a[0] != 1:
        a.insert(0,0)
    if a[-1] != n:
        a.append(n+1)
    print(a)
    ans = 0
    for i in range(1,len(a)):
        if a[i] - a[i-1] - 1 > 0:
            ans += (a[i] - a[i-1] - 1) // m
            if (a[i] - a[i-1] - 1) % m != 0:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if m == 0:
        print(1)
        return
    a.sort()
    # print(a)
    # print(n, m)
    # print(a)
    if a[0] != 1:
        a.insert(0, 0)
    if a[-1] != n:
        a.append(n+1)
    # print(a)
    b = []
    for i in range(len(a)-1):
        if a[i+1] - a[i] > 1:
            b.append(a[i+1] - a[i] - 1)
    # print(b)
    if len(b) == 0:
        print(0)
        return
    k = min(b)
    ans = 0
    for i in b:
        ans += (i+k-1)//k
    print(ans)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    B = []
    for i in range(M):
        if i == 0:
            B.append(A[i] - 1)
        else:
            B.append(A[i] - A[i-1] - 1)
        if i == M - 1:
            B.append(N - A[i])
    B.sort()
    k = B[0]
    ans = 0
    for i in range(M + 1):
        if B[i] % k == 0:
            ans += B[i] // k
        else:
            ans += B[i] // k + 1
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    d = []
    for i in range(1, m):
        d.append(a[i] - a[i - 1] - 1)
    d.sort()
    s = sum(d[:m - n])
    print(s + 1)
