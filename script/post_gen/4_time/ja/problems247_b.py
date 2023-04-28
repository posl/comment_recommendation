Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(b)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                print("Yes")
                return
    print("No")
main()

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    for i in range(n):
        if s[i] in t:
            if s[i] != t[i]:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 3

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
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print('Yes')
                    return
    print('No')

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
    for i in range(n):
        for j in range(n):
            if i != j and s[i] == s[j] and t[i] == t[j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 5

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
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 6

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
            if i != j:
                if s[i] == s[j]:
                    print("No")
                    return
                if t[i] == t[j]:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        name = input().split()
        s.append(name[0])
        t.append(name[1])
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def solve():
    N = int(input())
    s = []
    t = []
    for _ in range(N):
        a, b = input().split()
        s.append(a)
        t.append(b)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                return "Yes"
    return "No"

print(solve())

=======
Suggestion 9

def main():
    N = int(input())
    s = []
    t = []
    for i in range(0, N):
        s_t = input().split()
        s.append(s_t[0])
        t.append(s_t[1])
    for i in range(0, N):
        for j in range(0, N):
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    print(names)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][0] == names[j][1]:
                print('No')
                return
            if names[i][1] == names[j][0] or names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')
    return
