Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    print(min(N-1, happy+2*K))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(min(N-1, ans+2*K))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            ans += 1
    ans += min(2 * K, N - 1)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ans += 1
    ans += min(2 * k, n - 1)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int,input().split())
    S = input()
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    print(min(N-1, cnt+2*K))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        else:
            if S[i - 1] == S[i]:
                ans += 1
    ans += 2 * K
    ans = min(ans, N - 1)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    R = S.count('R')
    L = N - R
    ans = min(R, L) * 2 + min(K, abs(R-L))
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    s = input()
    if k == 1:
        print(max(s.count('R'), s.count('L')))
    else:
        s += 'R'
        c = 0
        for i in range(n):
            if s[i] == s[i + 1]:
                c += 1
        print(n - c)

=======
Suggestion 9

def solver(N, K, S):
    # Write your code here
    return 0
