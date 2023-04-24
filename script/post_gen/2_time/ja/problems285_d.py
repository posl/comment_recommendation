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
    if len(set(S)) == len(set(T)):
        print("Yes")
    else:
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
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == len(T_set):
        print("Yes")
    else:
        print("No")

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
    #print(S)
    #print(T)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == T[j] and T[i] == S[j]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    #print(S)
    #print(T)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == T[j]:
                print("No")
                return
    print("Yes")

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
    S = list(set(S))
    T = list(set(T))
    if len(S) == len(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = map(str,input().split())
        S.append(s)
        T.append(t)
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == len(T_set):
        print('Yes')
    else:
        print('No')

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
    #print(N, S, T)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j] or T[i] == T[j]:
                print("No")
                return
    print("Yes")

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
    print("Yes" if check(S, T) else "No")

=======
Suggestion 9

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if names[i][1] == names[j][0]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)

    # s と t が完全に一致している場合は、変更ができない
    if s == t:
        print("No")
        return

    # s と t が一致していない場合は、変更ができる
    print("Yes")
