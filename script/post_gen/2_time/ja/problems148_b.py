Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S, T = input().split()
    ans = ""
    for i in range(N):
        ans += S[i]
        ans += T[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s, t = input().split()
    ans = ""
    for i in range(n):
        ans += s[i]
        ans += t[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S, T = input().split()
    ans = []
    for i in range(N):
        ans.append(S[i])
        ans.append(T[i])
    print("".join(ans))

=======
Suggestion 5

def main():
    N = int(input())
    S, T = input().split()
    ans = []
    for i in range(N):
        ans.append(S[i])
        ans.append(T[i])
    print(''.join(ans))

=======
Suggestion 6

def main():
    N = int(input())
    S, T = input().split()

    ans = ''
    for i in range(N):
        ans += S[i]
        ans += T[i]

    print(ans)

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
    n = int(input())
    s, t = input().split()
    for i in range(n):
        print(s[i],t[i],sep='',end='')
    print()
