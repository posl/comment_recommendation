Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

main()

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-1-i])

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
    N = int(input())
    S = [input() for _ in range(N)]
    for s in S[::-1]:
        print(s)

=======
Suggestion 6

def main():
    N = int(input())
    s = [input() for i in range(N)]
    for i in range(N):
        print(s[N-1-i])
