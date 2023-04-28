Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n=int(input())
    ab=[]
    for _ in range(n):
        ai,bi=list(map(int,input().split()))
        ab.append((ai,bi))
    return n,ab

=======
Suggestion 2

def main():
    n = int(input())
    d = [0] * (10 ** 9 + 2)
    for _ in range(n):
        a, b = map(int, input().split())
        d[a] += 1
        d[a + b] -= 1
    for i in range(10 ** 9 + 1):
        d[i + 1] += d[i]
    print(*d[1: n + 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    C = [0] * (10 ** 9 + 2)
    for i in range(N):
        C[A[i]] += 1
        C[A[i] + B[i]] -= 1
    for i in range(10 ** 9 + 1):
        C[i + 1] += C[i]
    for i in range(1, N + 1):
        ans = 0
        for j in range(10 ** 9 + 1):
            if C[j] == i:
                ans += 1
        print(ans, end = " ")
    print()

=======
Suggestion 4

def solve(n, ab):
    d = {}
    for a, b in ab:
        d[a] = d.get(a, 0) + 1
        d[a + b] = d.get(a + b, 0) - 1
    result = [0] * n
    c = 0
    for i in range(1, 10**9 + 1):
        c += d.get(i, 0)
        result[c - 1] += 1
    return result

=======
Suggestion 5

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    days = [0] * (10**9 + 2)
    for i in range(N):
        days[A[i]] += 1
        days[A[i] + B[i]] -= 1
    for i in range(1, 10**9 + 2):
        days[i] += days[i - 1]
    ans = [0] * N
    for i in range(N):
        ans[days[A[i]] - 1] += 1
    print(*ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 1:
        print(B[N // 2] - A[N // 2] + 1)
    else:
        print((B[N // 2] + B[N // 2 - 1]) - (A[N // 2] + A[N // 2 - 1]) + 1)

=======
Suggestion 7

def main():
    N = int(input())
    D = [0] * (10**9 + 2)
    for _ in range(N):
        A, B = map(int, input().split())
        D[A] += 1
        D[A+B] -= 1
    for i in range(1, 10**9 + 1):
        D[i] += D[i-1]
    print(*D[1:10**9+1])

=======
Suggestion 8

def main():
    n = int(input())
    a = [0] * (n + 2)
    b = [0] * (n + 2)

    for i in range(1, n + 1):
        a[i], b[i] = map(int, input().split())

    s = [0] * (n + 2)
    for i in range(1, n + 1):
        s[a[i]] += 1
        s[a[i] + b[i]] -= 1

    for i in range(1, n + 1):
        s[i] += s[i - 1]

    for i in range(1, n + 1):
        print(s[i], end=' ')

    print()

=======
Suggestion 9

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_day = max(A) + max(B)
    day = [0] * (max_day + 1)
    for i in range(N):
        day[A[i] - 1] += 1
        day[A[i] + B[i] - 1] -= 1
    for i in range(max_day):
        day[i + 1] += day[i]
    for i in range(max_day):
        if day[i] > N:
            day[i] = N
    print(*day[:max_day], sep=" ")

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[0] = AB[0][1]
        else:
            ans[i] = ans[i-1] + AB[i][1]
    for i in range(N):
        if i == 0:
            print(ans[N-1])
        else:
            print(ans[N-1] - ans[i-1])
