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
            if i == j:
                continue
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return

    print("No")
    return

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
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
    for i in range(n):
        si, ti = input().split()
        for j in range(i+1, n):
            sj, tj = input().split()
            if si == sj and ti == tj:
                print("Yes")
                return
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
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
        s_i, t_i = map(str, input().split())
        s.append(s_i)
        t.append(t_i)
    
    if len(s) != len(set(s)) or len(t) != len(set(t)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name[i] == name[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name_list[i][0] == name_list[j][0] and name_list[i][1] == name_list[j][1]:
                print('Yes')
                return
    print('No')

=======
Suggestion 9

def main():
    N = int(input())
    names = []
    for _ in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1, N):
            if names[i] == names[j]:
                print('Yes')
                return
    print('No')
