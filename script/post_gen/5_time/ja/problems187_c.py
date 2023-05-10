Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S:
                return s[1:]
        else:
            if '!' + s in S:
                return s
    return 'satisfiable'

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s_set = set(s)
    for s_ in s:
        if s_[0] == '!':
            s_ = s_[1:]
        else:
            s_ = '!' + s_
        if s_ in s_set:
            print(s_)
            return
    print('satisfiable')
    return

=======
Suggestion 3

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    for i in s:
        if '!' + i in s:
            print(i)
            return
    print('satisfiable')

=======
Suggestion 4

def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S_set = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S_set:
                return s[1:]
        else:
            if '!' + s in S_set:
                return s

    return 'satisfiable'

print(solve())

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = "satisfiable"
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in S:
                ans = S[i][1:]
                break
        else:
            if "!" + S[i] in S:
                ans = S[i]
                break
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]

    if len(S) == len(set(S)):
        print("satisfiable")
    else:
        print("".join(S))

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] == '!' and S[i+1][0] != '!':
            if S[i][1:] == S[i+1]:
                print(S[i+1])
                return
        elif S[i][0] != '!' and S[i+1][0] == '!':
            if S[i] == S[i+1][1:]:
                print(S[i])
                return
    print('satisfiable')

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print(S[i])
            exit()
    print("satisfiable")

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_set = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S_set:
                print(s[1:])
                return
        else:
            if '!' + s in S_set:
                print(s)
                return
    print('satisfiable')

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i][0] == '!':
            if s[i+1] == s[i][1:]:
                print(s[i+1])
                exit()
    print('satisfiable')
