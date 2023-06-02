Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())
    S = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S:
                print(s[1:])
                return
        else:
            if '!'+s in S:
                print(s)
                return
    print('satisfiable')
solve()

=======
Suggestion 2

def judge(s):
    if s[0] == '!':
        s = s[1:]
    else:
        s = '!' + s
    return s

n = int(input())
s = []
for i in range(n):
    s.append(input())

s.sort()
for i in range(n-1):
    if s[i] == s[i+1]:
        print(s[i])
        exit()
print('satisfiable')

=======
Suggestion 3

def solve():
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
Suggestion 4

def main():
    N = int(input())
    s = [input() for i in range(N)]
    s = set(s)
    ans = "satisfiable"
    for i in s:
        if "!" + i in s:
            ans = i
            break
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s_set = set(s)
    for i in s_set:
        if i[0] == "!":
            if i[1:] in s_set:
                print(i[1:])
                return
        else:
            if "!"+i in s_set:
                print(i)
                return
    print("satisfiable")

=======
Suggestion 6

def solve():
    N = int(input())
    S = [input() for i in range(N)]
    S = set(S)
    for s in S:
        if '!' + s in S:
            return s
    return 'satisfiable'

print(solve())

=======
Suggestion 7

def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    s1 = set()
    s2 = set()
    for i in s:
        if i[0] == '!':
            s2.add(i[1:])
        else:
            s1.add(i)
    s = s1 & s2
    if len(s) == 0:
        print('satisfiable')
    else:
        print(s.pop())

=======
Suggestion 8

def solve():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    S = set(S)
    for s in S:
        if s[0] == "!":
            if s[1:] in S:
                print(s[1:])
                return
        else:
            if "!" + s in S:
                print(s)
                return
    print("satisfiable")

=======
Suggestion 9

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if "!" + s in S:
            print(s)
            exit()
    print("satisfiable")

=======
Suggestion 10

def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i][0] != '!' and s[i] == s[i+1] and s[i+1][0] == '!':
            return s[i]
    return 'satisfiable'
