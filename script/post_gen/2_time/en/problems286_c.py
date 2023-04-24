Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    s = input()
    count = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            count += 1
    if count == 0:
        print(0)
    elif count == 1:
        print(a)
    elif count == 2:
        print(min(a,b)*2)
    else:
        print((count-1)*b+a)

=======
Suggestion 2

def solve():
    N, A, B = map(int, input().split())
    S = input()
    for i in range(N//2):
        if S[i] != S[-i-1]:
            if S[i] == 'a':
                S = S[:i] + S[-i-1] + S[i+1:]
                A -= 1
            elif S[-i-1] == 'a':
                S = S[:i] + S[-i-1] + S[i+1:]
                A -= 1
            elif S[i] > S[-i-1]:
                S = S[:i] + S[-i-1] + S[i+1:]
                B -= 1
            else:
                S = S[:i] + S[-i-1] + S[i+1:]
                B -= 1
        if A < 0 or B < 0:
            return -1
    if N%2 == 1:
        if A > 0:
            S = S[:N//2] + 'a' + S[N//2+1:]
        elif B > 0:
            S = S[:N//2] + 'a' + S[N//2+1:]
        else:
            S = S[:N//2] + S[N//2] + S[N//2+1:]
    return A + B, S

=======
Suggestion 3

def solve():
    n, a, b = map(int, input().split())
    s = input()
    dp = [1e9] * (n + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            t = s[i:j]
            dp[j] = min(dp[j], dp[i] + b + (t != t[::-1]) * a)
    print(dp[n])

=======
Suggestion 4

def solve():
    n,a,b = map(int,input().split())
    s = input()
    dp = [float('inf')]*n
    dp[0] = a
    for i in range(1,n):
        dp[i] = min(dp[i], dp[i-1]+a)
        for j in range(1,i+1):
            if s[i-j] == s[i]:
                dp[i] = min(dp[i], dp[i-j-1]+b)
    print(dp[-1])

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    S = input()
    print(N, A, B)
    print(S)

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    S = input()

    dp = [0 for _ in range(N+1)]
    for i in range(N):
        dp[i+1] = dp[i] + A
        for j in range(i):
            if S[i-j-1] != S[i]:
                continue
            dp[i+1] = min(dp[i+1], dp[i-j-1]+B)
    print(dp[N])

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    S = input()
    print("No")

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    S = input()
    S = S[::-1]

    cnt = 0
    for i in range(N//2):
        if S[i] == S[N-1-i]:
            continue
        elif S[i] == "a":
            cnt += A
        elif S[i] == "b":
            cnt += B
        elif S[N-1-i] == "a":
            cnt += A
        elif S[N-1-i] == "b":
            cnt += B
        else:
            print(-1)
            return
    if N%2 == 1:
        if S[N//2] == "a":
            cnt += A
        elif S[N//2] == "b":
            cnt += B
    print(cnt)

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    s.reverse()
    count = 0
    for i in range(n):
        if i == 0:
            continue
        if s[i] == s[i - 1]:
            count += a
        else:
            count += b
    print(count)

=======
Suggestion 10

def make_palindrome(N, A, B, S):
    if N % 2 == 0:
        half = N // 2
        if S[:half] == S[half:]:
            return A * N
        else:
            return A * N + B
    else:
        half = N // 2
        if S[:half] == S[half+1:]:
            return A * N
        else:
            return A * N + B
