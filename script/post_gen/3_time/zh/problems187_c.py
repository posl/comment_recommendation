Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            print("存在")
            return
    print("可满足")

=======
Suggestion 2

def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S:
                print(s[1:])
                return
        else:
            if '!' + s in S:
                print(s)
                return
    print('satisfiable')

=======
Suggestion 3

def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if "!" + i in s:
            print(i)
            return
    print("satisfiable")

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                print(i[1:])
                exit()
        else:
            if ('!'+i) in s:
                print(i)
                exit()
    print('satisfiable')

=======
Suggestion 5

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if '!' + s in S:
            print(s)
            return
    print('satisfiable')

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = list(set(s))
    s.sort()
    s = [i[1:] for i in s if i[0] == '!']
    for i in s:
        if i in s:
            print(i)
            exit()
    print('satisfiable')

=======
Suggestion 7

def solve():
    N = int(input())
    S = []
    for i in range(N):
        s = input()
        if s[0] == '!':
            S.append(s[1:])
        else:
            S.append('!' + s)
    S.sort()
    for i in range(N - 1):
        if S[i][0] == '!' and S[i + 1][0] != '!':
            if S[i][1:] == S[i + 1]:
                print(S[i][1:])
                return
    print('satisfiable')
    return

=======
Suggestion 8

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = [x[1:] if x[0]=='!' else x for x in s]
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            return
    print('satisfiable')

=======
Suggestion 9

def main():
    n = int(input())
    s = [input() for i in range(n)]
    # print(s)
    s = set(s)
    # print(s)
    for i in s:
        if '!' + i in s:
            print(i)
            return
    print('satisfiable')

=======
Suggestion 10

def main():
    # import sys
    # readline = sys.stdin.readline
    # readline()
    # s = set()
    # for line in sys.stdin:
    #     if line.startswith('!'):
    #         if line[1:] in s:
    #             print(line[1:])
    #             return
    #     else:
    #         if '!' + line in s:
    #             print(line)
    #             return
    #         s.add(line)
    # print('satisfiable')
    import sys
    readline = sys.stdin.readline
    readline()
    s = set()
    for line in sys.stdin:
        if line.startswith('!'):
            if line[1:] in s:
                print(line[1:])
                return
        else:
            if '!' + line in s:
                print(line)
                return
            s.add(line)
    print('satisfiable')
