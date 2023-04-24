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
        print(S[N-i-1])

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
    S = [input() for i in range(N)]
    for i in range(N):
        print(S[N-i-1])

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        print(S[N - 1 - i])

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("

".join(s[::-1]))

=======
Suggestion 8

def main():
    N = int(input())
    list = []
    for i in range(N):
        list.append(input())
    for j in range(N):
        print(list[N-1-j])

main()

=======
Suggestion 9

def main():
    N = int(input())
    for i in range(N):
        S = input()
        print(S)
