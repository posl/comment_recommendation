Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                print("No")
                return
            if t[i] == t[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    s_t_list = [input().split() for _ in range(n)]
    for i in range(n):
        s_t_list[i].append(i)
    s_t_list = sorted(s_t_list, key=lambda x: x[0])
    s_list = [i[0] for i in s_t_list]
    t_list = [i[1] for i in s_t_list]
    index_list = [i[2] for i in s_t_list]
    for i in range(n-1):
        if t_list[i] == s_list[i+1]:
            continue
        else:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 3

def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(b)

    #print(s)
    #print(t)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == t[j]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a,b = input().split()
        s.append(a)
        t.append(b)
    for i in range(n):
        if s[i] == t[i]:
            print('No')
            exit()
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == t[j]:
                print('No')
                exit()
    print('Yes')
main()

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == T[j] and S[j] == T[i]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        if S[i] == T[i]:
            print('No')
            exit()
    for i in range(N):
        if S[i] in T[i+1:]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si,ti = input().split()
        s.append(si)
        t.append(ti)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j]:
                print('No')
                return
            if t[i] == t[j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)

    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] or t[i] == t[j]:
                print("No")
                return
    print("Yes")

main()

=======
Suggestion 9

def solve():
    #n = int(input())
    n = 5
    #s = []
    #t = []
    #for i in range(n):
    #    s.append(input())
    #    t.append(input())
    s = ['aaa', 'yyy', 'ccc', 'xxx', 'bbb']
    t = ['bbb', 'zzz', 'ddd', 'yyy', 'ccc']
    #print(n)
    #print(s)
    #print(t)
    #print(len(s))
    #print(len(t))
    #print(s[0])
    #print(t[0])
    #print(s[0] == t[0])
    #print(s[0] == t[1])
    #print(s[0] == t[2])
    #print(s[0] == t[3])
    #print(s[0] == t[4])
    #print(s[1] == t[0])
    #print(s[1] == t[1])
    #print(s[1] == t[2])
    #print(s[1] == t[3])
    #print(s[1] == t[4])
    #print(s[2] == t[0])
    #print(s[2] == t[1])
    #print(s[2] == t[2])
    #print(s[2] == t[3])
    #print(s[2] == t[4])
    #print(s[3] == t[0])
    #print(s[3] == t[1])
    #print(s[3] == t[2])
    #print(s[3] == t[3])
    #print(s[3] == t[4])
    #print(s[4] == t[0])
    #print(s[4] == t[1])
    #print(s[4] == t[2])
    #print(s[4] == t[3])
    #print(s[4] == t[4])
    #print(s[0] == s[1])
    #print(s[0] == s[2])
    #print(s[0] == s[3])
    #print(s[0] == s[4])
    #print(s[1] == s[2])
    #print(s[1] == s[3])
    #print

=======
Suggestion 10

def check(n, s, t):
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] or t[i] == t[j]:
                return False
    return True

n = int(input())

s = []
t = []

for i in range(n):
    a, b = input().split()
    s.append(a)
    t.append(b)
