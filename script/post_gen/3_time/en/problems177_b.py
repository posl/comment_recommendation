Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s) - len(t) + 1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = n
    for i in range(n - m + 1):
        cnt = 0
        for j in range(m):
            if s[i + j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = 10**9
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    ans = 10**9
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 5

def check(s, t, n, m):
    for i in range(n - m + 1):
        for j in range(m):
            if s[i + j] != t[j]:
                break
        else:
            return True
    return False

=======
Suggestion 6

def solve(S, T):
    N = len(S)
    M = len(T)
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return N - dp[N][M]

S = input()
T = input()
print(solve(S, T))

=======
Suggestion 7

def solve(s,t):
    n = len(s)
    m = len(t)
    res = m
    for i in range(n-m+1):
        cur = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cur += 1
        res = min(res,cur)
    return res

s = input()
t = input()
print(solve(s,t))

=======
Suggestion 8

def check(s, t, i):
    for j in range(len(t)):
        if s[i + j] != t[j]:
            return False
    return True

=======
Suggestion 9

def get_input():
    S = input()
    T = input()
    return S, T

=======
Suggestion 10

def find_min_changes(S, T):
    # Write your code here
    if len(T) > len(S):
        return -1
    min_changes = len(T)
    for i in range(len(S) - len(T) + 1):
        changes = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                changes += 1
        min_changes = min(min_changes, changes)
    return min_changes
