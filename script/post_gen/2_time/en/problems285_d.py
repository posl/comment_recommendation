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
        for j in range(i+1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print("No")
                return
    print("Yes")
    return

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
    
    return

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
        for j in range(i):
            if S[i] == S[j] or T[i] == T[j] or S[i] == T[j] or T[i] == S[j]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 4

def get_input():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    return N, S, T

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)

    if len(set(S)) != len(set(T)):
        print('No')
        return

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == T[j] and T[i] == S[j]:
                print('No')
                return

    print('Yes')
    return

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
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == N and len(T_set) == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) == len(S) and len(set(T)) == len(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == len(S) and len(T_set) == len(T) and len(S_set & T_set) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    #print(S, T)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j] or S[i] == T[j] or T[i] == S[j] or T[i] == T[j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 10

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)

    # 2つのリストを結合して、重複を削除する
    # 重複がなければ、すべてのユーザーがその名前を使える
    # 重複があれば、その名前を使うユーザーが存在する
    if len(set(S+T)) == len(S+T):
        print("Yes")
    else:
        print("No")
