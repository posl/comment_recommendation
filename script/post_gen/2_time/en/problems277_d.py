Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    cards = [0 for _ in range(M)]
    for a in A:
        cards[a] += 1
    for i in range(M):
        if cards[i] == 0:
            continue
        if cards[(i+1)%M] == 0:
            continue
        if cards[i] == 1 and cards[(i+1)%M] == 1:
            continue
        if cards[i] == 1:
            cards[i] -= 1
            cards[(i+1)%M] -= 1
            cards[(i+2)%M] += 1
        elif cards[(i+1)%M] == 1:
            cards[(i+1)%M] -= 1
            cards[(i+2)%M] -= 1
            cards[(i+3)%M] += 1
        else:
            cards[i] -= 2
            cards[(i+1)%M] -= 1
            cards[(i+2)%M] += 1
    ans = 0
    for i in range(M):
        if cards[i] == 0:
            continue
        if cards[i] == 1:
            ans += i
        else:
            ans += i*2
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(lambda x: int(x) % m, input().split()))
    c = [0] * m
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(m):
        if c[i] > 1:
            ans += min(i, m - i) * (c[i] - 1)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A.sort()
    if A[0] == 0:
        print(0)
        return
    if N == 1:
        print(A[0])
        return
    ans = 0
    for i in range(N-1):
        ans += min(A[i], M-A[i])
    ans += min(A[-1], M-A[-1])
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = (B[i] + A[i]) % M
    ans = 0
    for i in range(N-1,-1,-1):
        if A[i] == A[i-1]:
            continue
        if A[i] == M-1:
            continue
        if A[i] == M-2:
            ans += A[i] + 1
            continue
        if A[i] == M-3:
            ans += A[i] + 2
            continue
        if B[i+1] == 0:
            continue
        if B[i] == 0:
            ans += A[i] + 1
            continue
        if B[i] == 1:
            ans += A[i] + 2
            continue
        if B[i] == 2:
            ans += A[i] + 3
            continue
        if B[i] > 2:
            ans += A[i] + 4
            continue
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a % M for a in A]
    A = [a - M for a in A if a - M > 0] + A
    A = [a + M for a in A if a + M < 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()

    A = [a + M for a in A if a + M < 0] + A
    A = [a

=======
Suggestion 6

def solve(N, M, A):
    from collections import Counter
    A = [a % M for a in A]
    C = Counter(A)
    if M == 2:
        return min(C[0], C[1])
    if M == 3:
        return min(C[0], C[1], C[2])
    if M == 4:
        return min(C[0] + C[2], C[1] + C[3])
    if M == 5:
        return min(C[0] + C[3], C[1] + C[4], C[2])
    if M == 6:
        return min(C[0] + C[2] + C[4], C[1] + C[3] + C[5])
    if M == 7:
        return min(C[0] + C[3] + C[6], C[1] + C[4], C[2] + C[5])
    if M == 8:
        return min(C[0] + C[2] + C[4] + C[6], C[1] + C[3] + C[5] + C[7])
    if M == 9:
        return min(C[0] + C[3] + C[6], C[1] + C[4] + C[7], C[2] + C[5] + C[8])
    if M == 10:
        return min(C[0] + C[2] + C[4] + C[6] + C[8], C[1] + C[3] + C[5] + C[7] + C[9])
    if M == 11:
        return min(C[0] + C[3] + C[6] + C[9], C[1] + C[4] + C[7], C[2] + C[5] + C[8] + C[10])
    if M == 12:
        return min(C[0] + C[2] + C[4] + C[6] + C[8] + C[10], C[1] + C[3] + C[5] + C[7] + C[9] + C[11])

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    d = [0] * n
    for i in range(n):
        d[i] = (a[i+1] - a[i]) % m
    d.sort()
    ans = sum(d[:-1])
    print(ans)

main()

=======
Suggestion 8

def solve(n, m, a):
    cnt = [0] * m
    for i in a:
        cnt[i] += 1
    if cnt[0] > 0:
        return 1
    dp = [0] * m
    dp[0] = 1
    for i in range(1, m):
        if cnt[i] > 0:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]

=======
Suggestion 9

def solve(N, M, A):
    # write your code here
    B = [0]*M
    for a in A:
        B[a] += 1
    if M == 2:
        return 1 if B[1] > 0 else 0
    if M % 2 == 0:
        B[M//2] = min(B[M//2], 1)
    ans = 0
    for i in range(1, M//2+1):
        ans += min(B[i], B[M-i])*i
    return ans
