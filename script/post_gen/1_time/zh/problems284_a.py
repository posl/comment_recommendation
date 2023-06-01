Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 2

def reverse_print():
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
    list = []
    for i in range(n):
        list.append(input())
    for i in range(n):
        print(list[n-i-1])

main()

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.reverse()
    for i in range(n):
        print(s[i])

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(n):
        s = input()
        print(s[::-1])

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(n):
        print(input())

=======
Suggestion 8

def reverse_string(s):
    return s[::-1]

=======
Suggestion 9

def main():
    # N = int(input())
    # S = []
    # for i in range(N):
    #     S.append(input())
    # for i in range(N):
    #     print(S[N-i-1])
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.reverse()
    for i in range(N):
        print(S[i])

=======
Suggestion 10

def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    for i in range(n-1,-1,-1):
        print(s_list[i])
