Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S, T = input().split()
    ans = ""
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], end='')
        print(T[i], end='')
    print()

=======
Suggestion 3

def main():
    n = int(input())
    s, t = input().split()
    result = ''
    for i in range(n):
        result += s[i] + t[i]
    print(result)

=======
Suggestion 4

def main():
    N = int(input())
    S, T = input().split()

    ans = ""
    for i in range(N):
        ans += S[i]
        ans += T[i]

    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s, t = input().split()
    for i in range(n):
        print(s[i], t[i], sep='', end='')
    print()

=======
Suggestion 6

def main():
    n = int(input())
    s, t = input().split()
    print(''.join([s[i] + t[i] for i in range(n)]))

=======
Suggestion 7

def main():
    N = int(input())
    S, T = input().split()
    print("".join([S[i]+T[i] for i in range(N)]))

=======
Suggestion 8

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], end='')
    print()

=======
Suggestion 9

def main():
    N = int(input())
    S, T = input().split()
    print(''.join([s+t for s,t in zip(S,T)]))

=======
Suggestion 10

def main():
    N = int(input())
    S,T = input().split()
    print(''.join([x+y for x,y in zip(S,T)]))
