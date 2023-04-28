Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * m
    for i in range(n):
        b[a[i]] += 1
    c = [0] * m
    for i in range(m):
        c[i] = (m + i - 1) % m
    for i in range(m - 1):
        if b[i] > 0 and b[i + 1] > 0:
            b[i] -= 1
            b[i + 1] -= 1
            b[c[i]] += 1
    ans = 0
    for i in range(m):
        ans += i * b[i]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    for i in range(N):
        B[A[i]] += 1
    for i in range(M):
        if B[i] > 0:
            for j in range(M):
                if B[(i+j)%M] > 0:
                    B[(i+j)%M] -= 1
                    break
    ans = 0
    for i in range(M):
        ans += i * B[i]
    print(ans)
main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    ans = 0
    for i in range(N):
        l = i
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if A[m] - A[i] < M:
                l = m
            else:
                r = m
        ans = max(ans, B[l+1] - B[i])
    print(ans)

=======
Suggestion 4

def solve(N, M, A):
    # Write your code here
    return 0

N, M = map(int, input().split())
A = list(map(int, input().split()))
result = solve(N, M, A)
print(result)

=======
Suggestion 5

def solve():
    #import sys
    #input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = [0] * (M + 1)
    for i in range(N):
        C[A[i]] += 1
    ans = 0
    for i in range(M):
        if C[i] == 0 and C[(i + 1) % M] == 0:
            continue
        ans += C[i] * i
        C[(i + 1) % M] += C[i]
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.append(m)
    b = [0]*(n+1)
    for i in range(n):
        b[i] = a[i+1] - a[i] - 1
    b[n] = a[0] + m - a[n] - 1
    if m == 1:
        print(0)
        exit()
    if n == 1:
        if a[0] == 0 and a[1] == 1:
            print(0)
        else:
            print(1)
        exit()
    k = min(b)
    ans = 0
    for i in range(n+1):
        ans += (b[i] + k - 1)//k
    print(ans)

=======
Suggestion 7

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            if A[i] != B[-1]:
                B.append(A[i])
    N = len(B)
    if N == 1:
        return 0
    if N == 2:
        if (B[1] - B[0]) % M == 1:
            return 0
        else:
            return B[0] + B[1]
    if N == 3:
        if (B[1] - B[0]) % M == 1 and (B[2] - B[1]) % M == 1:
            return 0
        if (B[1] - B[0]) % M == 1:
            return B[2]
        if (B[2] - B[1]) % M == 1:
            return B[0]
        return B[0] + B[1] + B[2]
    if N == 4:
        if (B[1] - B[0]) % M == 1 and (B[2] - B[1]) % M == 1 and (B[3] - B[2]) % M == 1:
            return 0
        if (B[1] - B[0]) % M == 1 and (B[2] - B[1]) % M == 1:
            return B[3]
        if (B[2] - B[1]) % M == 1 and (B[3] - B[2]) % M == 1:
            return B[0]
        if (B[1] - B[0]) % M == 1 and (B[3] - B[2]) % M == 1:
            return B[2]
        if (B[1] - B[0]) % M == 1:
            return B[2] + B[3]
        if (B[2] - B[1]) % M == 1:
            return B[0] + B[3]
        if (B[3] - B[2]) % M == 1:

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (a[i+1] - a[i] - 1) % m
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    a.append(m)
    s = 0
    for i in range(n):
        s += a[i+1] - a[i] - 1
    print(s)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (a[i] + ans) % m
    print(ans)
