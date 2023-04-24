Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(N):
        for j in range(N):
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 2

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
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
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
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(N):
            if i != j and (S[i] == S[j] or T[i] == T[j]):
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
    for _ in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    for i in range(n):
        for j in range(n):
            if i != j and (s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]):
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(N):
            if i != j:
                if S[i] == S[j] or S[i] == T[j] or T[i] == S[j] or T[i] == T[j]:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 6

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                print("No")
                return
    print("Yes")

=======
Suggestion 7

def main():
    n = int(input())
    s = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], t[i] = input().split()
    ans = "Yes"
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                ans = "No"
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    data = [input().split() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if data[i][0] == data[j][0] or data[i][1] == data[j][1]:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 9

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(list(input().split()))
    for i in range(N):
        if name[i][0] in name[i][1] or name[i][1] in name[i][0]:
            continue
        else:
            for j in range(N):
                if i == j:
                    continue
                if name[i][0] in name[j] or name[i][1] in name[j]:
                    continue
                else:
                    print('No')
                    return
    print('Yes')

=======
Suggestion 10

def main():
    # 入力
    N = int(input())
    names = [input().split() for _ in range(N)]
    # 出力
    print('Yes' if solve(N, names) else 'No')
