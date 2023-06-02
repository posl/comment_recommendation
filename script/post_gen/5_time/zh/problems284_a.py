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

def problems284_a():
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
    S = []
    for i in range(N):
        S.append(input())
    S.reverse()
    for i in range(N):
        print(S[i])

=======
Suggestion 5

def reverse():
    n = int(input())
    for i in range(n):
        print(input()[::-1])

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
    num = int(input())
    str_list = []
    for i in range(num):
        str_list.append(input())
    for i in range(num):
        print(str_list[num-i-1])

=======
Suggestion 8

def main():
    num = int(input())
    lists = []
    for i in range(num):
        lists.append(input())
    lists.reverse()
    for i in lists:
        print(i)
