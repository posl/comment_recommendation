Synthesizing 10/10 solutions (Duplicates hidden)

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
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.reverse()
    for i in range(N):
        print(S[i])

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
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 6

def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    for i in range(n):
        print(list[n-i-1])

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        print(S[N - 1 - i])

=======
Suggestion 8

def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    for i in range(n):
        print(s_list[-1-i])

=======
Suggestion 9

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.reverse()
    print("\n".join(s))
