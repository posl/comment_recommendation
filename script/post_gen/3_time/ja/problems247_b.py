Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    s = [0] * N
    t = [0] * N
    for i in range(N):
        s[i], t[i] = input().split()
    for i in range(N):
        for j in range(N):
            if i != j:
                if s[i] == s[j] or t[i] == t[j]:
                    print("No")
                    exit()
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        a, b = input().split()
        s.append(a)
        t.append(b)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                print('No')
                return
    print('Yes')
    return

=======
Suggestion 3

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
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    a = []
    for i in range(n):
        if s[i] in t:
            a.append(s[i])
        else:
            a.append(t[i])
    if len(a) == len(set(a)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    names = [input().split() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 6

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][0] == names[j][1] or names[i][1] == names[j][0] or names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')
    return

=======
Suggestion 7

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_,t_ = input().split()
        s.append(s_)
        t.append(t_)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if s[i] == s[j] or t[i] == t[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    if len(s) == len(set(s)) and len(t) == len(set(t)):
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 9

def main():
    n = int(input())
    name = [input().split() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(list(input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][0] == names[j][1] or names[i][1] == names[j][0] or names[i][1] == names[j][1]:
                print("No")
                return
    print("Yes")
