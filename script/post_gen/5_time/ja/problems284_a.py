Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    for i in range(n-1,-1,-1):
        print(s[i])

main()

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
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-1-i])

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.reverse()
    print("\n".join(s))

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-i-1])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.reverse()
    for i in range(n):
        print(s[i])

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        print(s[n-1-i])
