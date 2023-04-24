Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s, t = input().split()
    ans = ""
    for i in range(n):
        ans += s[i]
        ans += t[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S, T = input().split()
    ans = ""
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s, t = input().split()
    ans = ''
    for i in range(n):
        ans += s[i]
        ans += t[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s, t = input().split()
    ans = ''
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s, t = input().split()
    for i in range(n):
        print(s[i], end="")
        print(t[i], end="")
    print()

=======
Suggestion 6

def main():
    N = int(input())
    S, T = input().split()
    print("".join([S[i] + T[i] for i in range(N)]))

=======
Suggestion 7

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], sep='', end='')
    print()

=======
Suggestion 8

def main():
    N = int(input())
    S, T = input().split()
    print(''.join(S[i] + T[i] for i in range(N)))

=======
Suggestion 9

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], sep="", end="")
    print()
