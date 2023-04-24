Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K):
            if i - A[j] >= 0:
                if dp[i - A[j]] == 0:
                    dp[i] = 1
                    break
    if dp[N] == 1:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K):
            if i - A[j] >= 0:
                dp[i] = max(dp[i], dp[i - A[j]] + 1)
    print(dp[N])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(K):
            if i - A[j] >= 0:
                dp[i] |= not dp[i-A[j]]
    print('Takahashi' if dp[N] else 'Aoki')

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [0] * (N+1)
    for i in range(1, N+1):
        for a in A:
            if i - a >= 0 and dp[i-a] == 0:
                dp[i] = 1
                break

    print("Takahashi" if dp[N] else "Aoki")

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N+1)
    for i in range(N):
        if dp[i] == 0:
            for a in A:
                if i+a <= N:
                    dp[i+a] = 1
    if dp[N] == 1:
        print("Second")
    else:
        print("First")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        if i in A:
            dp[i] = 0
            continue
        for a in A:
            if i - a >= 0:
                if dp[i - a] == 0:
                    dp[i] = 1
                    break
    print(dp[N])

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    dp = [False] * (N+1)
    dp[0] = True
    for i in range(N+1):
        if dp[i] == True:
            for j in range(K):
                if i + A[j] <= N:
                    dp[i + A[j]] = True
    print(N - dp[::-1].index(True))

=======
Suggestion 8

def main():
    import sys
    readline = sys.stdin.readline
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K):
            if i - A[j] < 0:
                break
            if dp[i - A[j]] == 0:
                dp[i] = 1
                break
    print(dp[N] * "Takahashi" or "Aoki")

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.reverse()
    for a in A:
        if N % a == 0:
            print(N - a)
            break
        else:
            N -= N % a
