Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            ans += 1
    print(ans)

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
    ans = 1
    for i in range(1,N):
        if S[i] != S[i-1]:
            ans += 1
    print(ans)

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
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans+1)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(N):
        if i == 0:
            continue
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(input())

    if N == 1:
        print(1)
        return

    i = 0
    while i < N-1:
        if S[i] == S[i+1]:
            S.pop(i)
            N -= 1
        else:
            i += 1

    print(N)
