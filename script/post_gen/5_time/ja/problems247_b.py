Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    names = [input().split() for i in range(n)]
    names = [name[0] + ' ' + name[1] for name in names]
    for i in range(n):
        for j in range(n):
            if i != j and names[i] == names[j]:
                print('Yes')
                return
    print('No')

=======
Suggestion 2

def judge(n, s, t):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                return 'Yes'
    return 'No'

n = int(input())
s = []
t = []
for i in range(n):
    s_i, t_i = input().split()
    s.append(s_i)
    t.append(t_i)

print(judge(n, s, t))

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
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        (s_i, t_i) = map(str, input().split())
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    s_t = [input().split() for _ in range(N)]
    s = [s_t[i][0] for i in range(N)]
    t = [s_t[i][1] for i in range(N)]
    ans = 'No'
    for i in range(N):
        if s[i] != t[i]:
            if s[i] in t:
                ans = 'Yes'
                break
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    for i in range(n):
        for j in range(n):
            if i != j and (s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]):
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 7

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
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 8

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
            if i != j and (s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]):
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def get_input():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    return n, s, t

=======
Suggestion 10

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] and t[i] == t[j]:
                print("No")
                return

    print("Yes")

main()
