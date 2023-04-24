Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1,N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    if n == 1:
        print(1)
        return
    cnt = 1
    for i in range(1, n):
        if s[i-1] != s[i]:
            cnt += 1
    print(cnt)

main()

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    print(N - S.count(S[0]) - S.count(S[-1]) + 1)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    print(len(set(S)))
