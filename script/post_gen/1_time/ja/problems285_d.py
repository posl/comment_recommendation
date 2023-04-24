Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
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
    if len(set(S)) == len(set(T)):
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
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j] or T[i] == T[j] or S[i] == T[j] or T[i] == S[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 4

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
    for i in range(N-1):
        for j in range(i+1, N):
            if T[i] == T[j]:
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
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) != len(set(T)):
        print("No")
        return
    print("Yes")

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
    s_set = set(s)
    t_set = set(t)
    if len(s_set) == len(t_set):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    print('Yes' if solve(N, S, T) else 'No')

=======
Suggestion 8

def main():
    N = int(input())
    users = []
    for i in range(N):
        users.append(input().split())
    #print(users)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if users[i][0] == users[j][1]:
                print("No")
                return
    print("Yes")

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    
    # 2人以上のユーザが同じユーザ名を希望する場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を希望するユーザがいないかを確認する
    if len(S) != len(set(S)) or len(T) != len(set(T)):
        print("No")
        exit()
    
    # 2人以上のユーザが同じユーザ名を現在のユーザ名としている場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を現在のユーザ名としているユーザがいないかを確認する
    if len(set(S)) != len(set(T)):
        print("No")
        exit()
    
    # 2人以上のユーザが同じユーザ名を現在のユーザ名としている場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を現在のユーザ名としているユーザがいないかを確認する
    if len(set(S)) != len(set(T)):
        print("No")
        exit()
    
    # 2人以上のユーザが同じユーザ名を現在のユーザ名としている場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を現在のユーザ名としているユーザがいないかを確認

=======
Suggestion 10

def main():
    N = int(input())
    user = []
    for i in range(N):
        user.append(input().split())
    #print(user)
    for i in range(N):
        #print("i:",i)
        for j in range(N):
            #print("j:",j)
            if i == j:
                continue
            if user[i][0] == user[j][1]:
                print("No")
                return
    print("Yes")
    return

main()
