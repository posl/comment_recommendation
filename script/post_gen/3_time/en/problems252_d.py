Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if A[i] != A[j] != A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    if a[i] + a[j] > a[k]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200001
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(200001):
        if B[i] >= 2:
            ans += B[i] * (B[i] - 1) // 2
    for a in A:
        print(ans - (B[a] - 1))

main()

I s

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        k = i+2
        for j in range(i+1, n-1):
            while k < n and a[i]+a[j] > a[k]:
                k += 1
            ans += k - j - 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        if A[i] == A[i+1]:
            continue
        for j in range(i+1, N-1):
            if A[j] == A[j+1]:
                continue
            for k in range(j+1, N):
                if A[k] == A[k-1]:
                    continue
                if A[i] + A[j] > A[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += bisect.bisect_left(a, a[i] + 3) - i - 1
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A

    from collections import Counter
    counter = Counter(A)

    if any([v >= 3 for v in counter.values()]):
        print(0)
        return

    # dp[i][j] = i番目までの数を使って、j個の数字を使った場合の組み合わせの数
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(N + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= 1:
                dp[i][j] += dp[i - 1][j - 1]

    ans = 0
    for i in range(1, N + 1):
        ans += dp[N][i] * i
    print(ans)
