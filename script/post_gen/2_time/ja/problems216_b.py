Synthesizing 10/10 solutions (Duplicates hidden)

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
        for j in range(i+1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return
    print("No")

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
        for j in range(N):
            if i != j:
                if S[i] == S[j] and T[i] == T[j]:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    T = []
    for n in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                s1, t1 = input().split()
                s2, t2 = input().split()
                if s1 == s2 and t1 == t2:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input().split()[0])
        t.append(input().split()[0])
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    names = [input().split() for _ in range(n)]
    names.sort()
    for i in range(1, n):
        if names[i][0] == names[i-1][0] and names[i][1] == names[i-1][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    N = int(input())
    names = list()
    for i in range(N):
        names.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if names[i] == names[j]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 9

def main():
    n = int(input())
    # 2次元配列に格納
    name = [[input() for i in range(2)] for j in range(n)]
    # 2次元配列を1次元配列に変換
    name = [name[i][0] + name[i][1] for i in range(n)]
    # 重複を削除
    name = set(name)
    # 重複がある場合はYes, ない場合はNo
    if len(name) < n:
        print("Yes")
    else:
        print("No")
