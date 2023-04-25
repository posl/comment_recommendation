Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count("1") != K:
            continue
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += A[j]
        S.add(s)
    ans = -1
    for s in S:
        if s % D == 0:
            ans = max(ans, s)
    print(ans)

main()

=======
Suggestion 2

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    ans = -1
    for i in S:
        if i % D == 0:
            ans = max(ans, i)
    print(ans)

=======
Suggestion 3

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = {0}
    for i in range(K):
        S = {a+b for a in S for b in A if a+b <= D}
    print(max(S) if max(S) % D == 0 else -1)

=======
Suggestion 4

def solve():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (d + 1)
    for i in range(d + 1):
        for j in range(k):
            if i - a[j] >= 0:
                dp[i] = dp[i] or not dp[i - a[j]]
    if dp[d]:
        print(d)
    else:
        print(-1)

=======
Suggestion 5

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(2**N):
        S.add(sum([A[j] for j in range(N) if ((i>>j) & 1)]))
    S = sorted([s for s in S if s % D == 0])
    if len(S) == 0:
        print(-1)
    else:
        print(S[-1])

=======
Suggestion 6

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    ans = -1
    for i in range(2 ** N):
        if bin(i).count('1') != K:
            continue
        S = 0
        for j in range(N):
            if (i >> j) & 1:
                S += A[j]
        if S % D == 0:
            ans = max(ans, S)
    print(ans)

=======
Suggestion 7

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    S = set()
    for i in range(K):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    ans = -1
    for s in S:
        if s % D == 0:
            ans = s
    print(ans)

=======
Suggestion 8

def main():
    # Read data
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))

    # Compute the set of sums
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])

    # Find the greatest multiple of D in S
    ans = -1
    for x in S:
        if x % D == 0:
            ans = max(ans, x)

    # Print the answer
    print(ans)

main()

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))
