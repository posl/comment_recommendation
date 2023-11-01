Synthesizing 10/10 solutions

=======
Suggestion 1

def problem187c():
    n = int(input())
    s = [input() for _ in range(n)]
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                return i[1:]
    return 'satisfiable'

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i][0] == '!' and s[i+1][0] != '!':
            if s[i][1:] == s[i+1]

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if '!' + i in s:
            print(i)
            return
    print(

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s_set = set(s)
    for s_i in s:
        if s_i[0] == "!":
            if s_i[1:] in s_set:
                print(s

=======
Suggestion 5

def main():
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    for i in s:
        if "!" + i in s:
            print(i)
            return
    print("satisfiable")

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = list(set(s))
    s.sort()
    for i in range(len(s)):
        if s[i][0] == '!':
            if s[i][1:] in s:
                print(s[

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] == '!' and S[i+1] == S[i][1:]:
            print(S[i][1:])

=======
Suggestion 8

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = sorted(s)
    for i in range(n-1):
        if s[i][0] != '!' and s[i+1][0] == '!' and s[i] == s[i+1][1:]:
            print(s[i])

=======
Suggestion 9

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    for i in s:
        if '!' + i in s:
            print(i)
            break
    else:
        print('satisfiable')

=======
Suggestion 10

def problem187_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    for i in range(n):
        if s[i][0] == "!":
            s[i] = s[i][1:]
    s.sort()

    for i in range
