Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.reverse()
    for i in range(N):
        print(S[i])

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        print(S[N-1-i])

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        print(S[N-1-i])

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        print(s[n-1-i])

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.reverse()
    for s in S:
        print(s)
