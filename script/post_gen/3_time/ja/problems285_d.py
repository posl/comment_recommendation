Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif S[i] == T[j]:
                print('No')
                exit()
    print('Yes')

=======
Suggestion 2

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
            if S[i] == S[j] or T[i] == T[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 3

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
            if S[i] == S[j] or T[i] == T[j]:
                print('No')
                exit()

    print('Yes')

=======
Suggestion 4

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
            if s[i] == t[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    s = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], t[i] = input().split()
    for i in range(n):
        for j in range(n):
            if i != j and s[i] == s[j]:
                print('No')
                return
    for i in range(n):
        for j in range(n):
            if i != j and s[i] == t[j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        if S[i] in T:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    flag = True
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == T[j] and S[j] == T[i]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) == N and len(set(T)) == N:
        for i in range(N):
            if S[i] == T[i]:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)

    for i in range(n):
        if s[i] == t[i]:
            print("No")
            return

    for i in range(n):
        for j in range(i+1, n):
            if s[i] == t[j] and s[j] == t[i]:
                print("No")
                return

    print("Yes")
    return

=======
Suggestion 10

def main():
    n = int(input())
    s_t = []
    for i in range(n):
        s_t.append(input().split())
    s_t2 = s_t.copy()
    for i in range(n):
        s_t2[i][0], s_t2[i][1] = s_t2[i][1], s_t2[i][0]
    s_t2.sort()
    for i in range(n):
        s_t[i][0], s_t[i][1] = s_t[i][1], s_t[i][0]
    s_t.sort()
    #print(s_t)
    #print(s_t2)
    for i in range(n):
        if s_t[i][0] != s_t2[i][0] or s_t[i][1] != s_t2[i][1]:
            print("No")
            exit()
    print("Yes")
