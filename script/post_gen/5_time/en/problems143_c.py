Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans+1)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(1, N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans+1)

main()
