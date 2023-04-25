Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 2

def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
    for i in range(N):
        for j in range(N):
            if i != j:
                if S[i] == S[j] or T[i] == T[j]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 3

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    if len(set(s)) == len(set(t)) == len(set(s + t)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][0] == names[j][1] or names[i][1] == names[j][0] or names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')

=======
Suggestion 5

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    if len(s) == len(set(s)) and len(t) == len(set(t)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or t[i] == t[j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 7

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 8

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 9

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    if len(s) != len(set(s)) or len(t) != len(set(t)):
        print("No")
        return
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] and t[i] == t[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    name = sorted(name, key=lambda x: (x[0], x[1]))
    for i in range(N-1):
        if name[i][0] == name[i+1][0] and name[i][1] == name[i+1][1]:
            print('No')
            return
    print('Yes')
