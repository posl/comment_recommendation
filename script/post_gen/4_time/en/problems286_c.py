Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            if S[i] == 'a':
                ans += A
            elif S[i] == 'b':
                ans += B
            elif S[i] == 'c':
                ans += A+B
            elif S[N-1-i] == 'a':
                ans += A
            elif S[N-1-i] == 'b':
                ans += B
            elif S[N-1-i] == 'c':
                ans += A+B
    if N%2 == 1 and S[N//2] != 'c':
        if S[N//2] == 'a':
            ans += A
        elif S[N//2] == 'b':
            ans += B
    print(ans)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n//2):
        if s[i] == s[-(i+1)]:
            continue
        if s[i] == 'a':
            ans += a
        elif s[i] == 'b':
            ans += b
        elif s[-(i+1)] == 'a':
            ans += a
        elif s[-(i+1)] == 'b':
            ans += b
        else:
            print(-1)
            return
    if n % 2 == 1:
        if s[n//2] == 'a':
            ans += a
        elif s[n//2] == 'b':
            ans += b
    print(ans)

=======
Suggestion 3

def main():
    N,A,B = map(int,input().split())
    S = input()
    ans = 0
    for i in range(N//2):
        if S[i] == S[-i-1]:
            continue
        if S[i] == 'a':
            ans += A
        elif S[i] == 'b':
            ans += B
        else:
            print(-1)
            return
    if N % 2 == 1 and S[N//2] != 'a' and S[N//2] != 'b':
        print(-1)
        return
    print(ans)

=======
Suggestion 4

def main():
    # input
    n, a, b = map(int, input().split())
    s = input()

    # compute
    ans = 0
    for i in range(n//2):
        if s[i] == s[n-1-i]:
            continue
        elif s[i] == 'a':
            if s[n-1-i] == 'b':
                ans += a
            else:
                ans += b
        elif s[i] == 'b':
            if s[n-1-i] == 'a':
                ans += a
            else:
                ans += b
        else:
            if s[n-1-i] == 'a':
                ans += b
            else:
                ans += a

    # output
    print(ans)

=======
Suggestion 5

def main():
    # input
    n, a, b = map(int, input().split())
    s = input()

    # compute
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = dp[i] + a
        for j in range(i):
            if s[i] == s[j]:
                dp[i + 1] = min(dp[i + 1], dp[j] + b)
    ans = dp[n]

    # output
    print(ans)

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    s = input()
    print(1)

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    s = input()
    return 0

=======
Suggestion 8

def main():
    N,A,B = map(int,input().split())
    S = input()
    print(0)

=======
Suggestion 9

def palindrome(s):
    return s == s[::-1]

=======
Suggestion 10

def get_input():
    return map(int, raw_input().split())
