Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S, T = input().split()
    result = ""
    for i in range(N):
        result += S[i] + T[i]
    print(result)

=======
Suggestion 2

def main():
    n = int(input())
    s, t = input().split()
    for i in range(n):
        print(s[i], end='')
        print(t[i], end='')
    print()

=======
Suggestion 3

def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i]
        ans += T[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s,t = input().split()
    ans = ""
    for i in range(n):
        ans += s[i]
        ans += t[i]
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    s, t = input().split()
    ans = ''
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s, t = input().split()
    result = ''
    for i in range(n):
        result += s[i] + t[i]
    print(result)

=======
Suggestion 7

def problems148_b():
    n = int(input())
    s, t = input().split()
    result = ""
    for i in range(n):
        result += s[i]
        result += t[i]
    print(result)

=======
Suggestion 8

def main():
    N = int(input())
    S,T = input().split()
    for i in range(N):
        print(S[i]+T[i],end='')
    print()

=======
Suggestion 9

def main():
    n = int(input())
    s, t = input().split(' ')
    result = ''
    for i in range(n):
        result = result + s[i] + t[i]
    print(result)
