Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print("存在")
            return
    print("不存在")
    return

=======
Suggestion 2

def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            exit()
    print("satisfiable")

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i][0] == '!':
            s[i] = s[i][1:]
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            exit()
    print('satisfiable')

=======
Suggestion 4

def solve(n, s):
    s1 = set()
    s2 = set()
    for i in range(n):
        if s[i][0] == '!':
            s1.add(s[i][1:])
        else:
            s2.add(s[i])
    for i in s2:
        if i in s1:
            return i
    return 'satisfiable'

n = int(input())
s = []
for i in range(n):
    s.append(input())
print(solve(n, s))

=======
Suggestion 5

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S = [s.lstrip('!') for s in S]
    S = set(S)

    for s in S:
        if '!' + s in S:
            return s
    return 'satisfiable'

=======
Suggestion 6

def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    s1 = set()
    s2 = set()
    for s in ss:
        if s[0] == '!':
            s1.add(s[1:])
        else:
            s2.add(s)
    for s in s1:
        if s in s2:
            print(s)
            return
    print('satisfiable')

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if '!' + i in s:
            print(i)
            break
    else:
        print('satisfiable')

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s_set = set(s)
    for i in s_set:
        if i[0] == '!':
            if i[1:] in s_set:
                print(i[1:])
                return
        else:
            if '!' + i in s_set:
                print(i)
                return
    print('satisfiable')

=======
Suggestion 9

def solve():
    N = int(input())
    S = [input() for i in range(N)]
    S = [s[1:] if s[0] == '!' else s for s in S]
    S.sort()
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            print(S[i])
            return
    print('satisfiable')

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = list(set(s))
    for i in range(len(s)):
        if s[i][0] == '!':
            if s[i][1:] in s:
                print(s[i][1:])
                exit()
        else:
            if '!' + s[i] in s:
                print(s[i])
                exit()
    print('satisfiable')
main()
