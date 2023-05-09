Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = set()
    for i in range(N):
        s = input()
        if s[0] == '!':
            if s[1:] in S:
                print(s[1:])
                return
            else:
                S.add(s)
        else:
            if '!' + s in S:
                print(s)
                return
            else:
                S.add(s)

    print('satisfiable')

=======
Suggestion 2

def solve():
    N = int(input())
    S = set()
    for _ in range(N):
        s = input()
        if s[0] == '!':
            if s[1:] in S:
                print(s[1:])
                return
            else:
                S.add(s)
        else:
            if '!' + s in S:
                print(s)
                return
            else:
                S.add(s)
    print('satisfiable')

=======
Suggestion 3

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    for i in s:
        if "!" + i in s:
            print(i)
            return
    print("satisfiable")

=======
Suggestion 4

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
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S2 = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S2:
                print(s[1:])
                return
        else:
            if '!' + s in S2:
                print(s)
                return
    print('satisfiable')

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S_set = set(S)
    for i in range(N):
        if S[i][0] == '!':
            if S[i][1:] in S_set:
                print(S[i][1:])
                break
        else:
            if '!' + S[i] in S_set:
                print(S[i])
                break
    else:
        print('satisfiable')

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = sorted(s)
    for i in range(n-1):
        if s[i][0] == "!" and s[i+1] == s[i][1:]:
            print(s[i+1])
            return
    print("satisfiable")

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    
    for i in range(n-1):
        if s[i][0] != '!' and s[i] == s[i+1]:
            print(s[i])
            return
        if s[i][0] == '!' and s[i][1:] == s[i+1]:
            print(s[i+1])
            return
    print('satisfiable')

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    
    s.sort()
    for i in range(n):
        if s[i][0] == '!':
            if s[i][1:] in s:
                print(s[i][1:])
                exit()
        else:
            if '!' + s[i] in s:
                print(s[i])
                exit()
    print('satisfiable')
