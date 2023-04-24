Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N-1, -1, -1):
        print(S[i])

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-1-i])

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 4

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l.reverse()
    for i in l:
        print(i)

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        print(S[N-i-1])

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        print(S[N - 1 - i])

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(*s[::-1], sep='

')

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        print(S[-i-1])

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(n):
        print(input())
