Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.reverse()
    for i in range(n):
        print(s[i])

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
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-i-1])
main()

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for s in S[::-1]:
        print(s)

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(*S[::-1], sep='

')

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        print(s[n - i - 1])

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print('

'.join(s[::-1]))

=======
Suggestion 8

def main():
    n = int(input())
    for i in range(n):
        s = input()
        print(s)

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(n):
        print(input())

=======
Suggestion 10

def main():
    n = int(input())
    print('

'.join([input() for i in range(n)][::-1]))
