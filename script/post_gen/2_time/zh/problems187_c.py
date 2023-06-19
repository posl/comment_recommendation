Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    s.sort()
    #print(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
            print("存在不满足的字符串")
            print(s[i])
            return
    print("可满足")
    return

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

solve()

=======
Suggestion 3

def solve():
    #n = int(input())
    #s = [input() for _ in range(n)]
    n = 6
    s = ['a', '!a', 'b', '!c', 'd', '!d']
    #n = 10
    #s = ['red', 'red', 'red', '!orange', 'yellow', '!blue', 'cyan', '!green', 'brown', '!gray']
    a = set()
    for i in range(n):
        if s[i][0] == '!':
            a.add(s[i][1:])
        else:
            a.add('!' + s[i])
    for i in range(n):
        if s[i] in a:
            print(s[i])
            break
    else:
        print('satisfiable')

=======
Suggestion 4

def solve():
    N = int(input())
    S = [input() for _ in range(N)]

    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == '!':
            S1.add(s[1:])
        else:
            S2.add(s)

    for s in S1:
        if s in S2:
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

    S = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S:
                return print(s[1:])
        else:
            if '!'+s in S:
                return print(s)
    print('satisfiable')

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    for s in S:
        if "!" + s in S:
            print(s)
            return
    print("satisfiable")

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if '!' + i in s:
            print(i)
            exit()
    print('satisfiable')

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    S = set(S)
    for s in S:
        if '!' + s in S:
            print(s)
            return
    print('satisfiable')

=======
Suggestion 9

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s2 = []
    for i in range(N):
        if s[i][0] == '!':
            s2.append(s[i][1:])
        else:
            s2.append('!' + s[i])
    s2.sort()
    for i in range(N-1):
        if s2[i] == s2[i+1]:
            print(s2[i][1:])
            exit()
    print('satisfiable')

=======
Suggestion 10

def problem187_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    for i in range(n):
        if s[i][0] == "!":
            if s[i][1:] in s:
                print(s[i][1:])
                break
        else:
            if "!" + s[i] in s:
                print(s[i])
                break
    else:
        print("satisfiable")
