Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] != '!':
            if S[i][0] == S[i+1][0]

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                pr

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = set(s)
    for i in s:
        if '!' + i in s:
            print(i)
            break
    else:
        print('satisfiable')

=======
Suggestion 5

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
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if s[0] == '!':
            s = s[1:]
            if s in S:
                print(s)

=======
Suggestion 7

def solve():
    n = int(input())
    s = set()
    for i in range(n):
        si = input()
        if si[0] == '!':
            if si[1:] in s:
                print(si[1:])
                return

=======
Suggestion 8

def main():
    # 输入
    N = int(input())
    S = [input() for i in range(N)]
    # 判断
    for i in S:
        if '!' + i in S:
            print(i)
            return
    print('satisfiable')

=======
Suggestion 9

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s_set = set(s)
    for i in range(n):
        if s[i][0] == '!':
            if s[i][1:] in s_set:
                print
