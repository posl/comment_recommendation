Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i >= a and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    print(dp[-1])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i - A[j] >= 0 and dp[i - A[j]] != -1:
                dp[i] = max(dp[i], dp[i - A[j]] * 10 + A[j])
    print(dp[N])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(M):
            if i + A[j] <= N:
                dp[i + A[j]] = max(dp[i + A[j]], dp[i] * 10 + A[j])
    print(dp[N])

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(M):
            if i + match[A[j]] <= N:
                dp[i + match[A[j]]] = max(dp[i + match[A[j]]], dp[i] * 10 + A[j])
    print(dp[N])

match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
solve()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    matchsticks = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (N + 1)
    dp[0] = 0
    prev = [-1] * (N + 1)
    for i in range(N + 1):
        if dp[i] < 0:
            continue
        for j in range(M):
            if i + matchsticks[A[j] - 1] <= N:
                if dp[i + matchsticks[A[j] - 1]] < dp[i] * 10 + A[j]:
                    dp[i + matchsticks[A[j] - 1]] = dp[i] * 10 + A[j]
                    prev[i + matchsticks[A[j] - 1]] = A[j]
    ans = []
    i = N
    while i > 0:
        ans.append(prev[i])
        i -= matchsticks[prev[i] - 1]
    ans.reverse()
    print(''.join(map(str, ans)))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A = [str(a) for a in A]
    A = ''.join(A)
    #print(A)
    #pri

=======
Suggestion 7

def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.sort(reverse=True)
    A = [x for x in A if x != 1]
    S = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    D = [[0, 0] for _ in range(N+1)]
    for i in range(1, N+1):
        for a in A:
            if i - S[a] >= 0 and D[i-S[a]][0] + 1 > D[i][0]:
                D[i] = [D[i-S[a]][0] + 1, a]
    ans = ''
    i = N
    while i > 0:
        ans += str(D[i][1])
        i -= S[D[i][1]]
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A = [str(a) for a in A]
    match = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    ans = ""
    for i in range(9, 0, -1):
        if match[i] <= N and str(i) in A:
            ans += str(i) * (N // match[i])
            N %= match[i]
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a = [str(i) for i in a]
    #print(a)
    #print(a[0])
    #print(a[0] * (n // len(a[0])))
    #print(a[0] * (n // len(a[0])) + a[0][:n % len(a[0])])
    print(a[0] * (n // len(a[0])) + a[0][:n % len(a[0])])

=======
Suggestion 10

def makeInt(N, M, A):
    # N: length of matchstick
    # M: number of digits
    # A: digits

    # digit: matchstick
    digit = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    # dp[i]: maximum number of matchstick
    # dp[i]: maximum number of matchstick
    dp = [-1] * (N + 1)
    dp[0] = 0
    # dp[i]: maximum number of matchstick
    digitList = [-1] * (N + 1)
    digitList[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(M):
            if i + digit[A[j]] <= N:
                if dp[i + digit[A[j]]] < dp[i] * 10 + A[j]:
                    dp[i + digit[A[j]]] = dp[i] * 10 + A[j]
                    digitList[i + digit[A[j]]] = A[j]
    return digitList[N]
