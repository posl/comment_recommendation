Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    first_line = input()
    second_line = input()
    return first_line, second_line

=======
Suggestion 2

def find(a):
    if a not in dic:
        dic[a] = a
        return a
    if dic[a] == a:
        return a
    else:
        dic[a] = find(dic[a])
        return dic[a]

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    users = [0] * N
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            users[A - 1] |= 1 << (B - 1)
        elif T == 2:
            users[A - 1] &= ~(1 << (B - 1))
        else:
            print("Yes" if users[A - 1] & (1 << (B - 1)) and users[B - 1] & (1 << (A - 1)) else "No")

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    #print(N, Q)
    #print(T)
    #print(A)
    #print(B)
    #print(T[0], A[0], B[0])
    #print(T[1], A[1], B[1])
    #print(T[2], A[2], B[2])

    #判断用户A_i和B_i是否在互相关注
    #用户A_i跟随用户B_i，用户B_i跟随用户A_i
    #if T_i = 3：意味着要求你确定用户A_i和B_i是否在互相关注。  如果用户A_i跟随用户B_i，用户B_i跟随用户A_i，你需要打印Yes，否则打印No。
    #如果T_i=1：意味着用户A_i关注了用户B_i。  如果用户A_i在此操作时已经在关注用户B_i，它不会做任何改变。
    #如果T_i = 2：意味着用户A_i取消对用户B_i的关注。  如果用户A_i在此操作时没有关注用户B_i，它不会做任何改变。

    #用户关注用户
    #用户取消关注用户
    #用户判断用户是否在互相关注
    #用户关注用户
    #用户取消关注用户
    #用户取消关注用户
    #用户取消关注用户
    #用户判断用户是否在互相关注
    #用户取消关注用户
    #用户取消关注用户
    #用户关注用户
    #用户关注用户
    #用户取消关注用户
    #用户判断用户是否在互相关注
    #用户取消关注用户
    #用户取消关注用户
    #用户取消关注用户
    #用户判断

=======
Suggestion 6

def get_input():
    N, Q = map(int, input().split())
    t = []
    a = []
    b = []
    for i in range(Q):
        t1, a1, b1 = map(int, input().split())
        t.append(t1)
        a.append(a1)
        b.append(b1)
    return N, Q, t, a, b

=======
Suggestion 7

def main():
    n,q = map(int, input().split())
    follow = set()
    for i in range(q):
        t,a,b = map(int, input().split())
        if t == 1:
            follow.add((a,b))
        elif t == 2:
            follow.discard((a,b))
        elif t == 3:
            if (a,b) in follow and (b,a) in follow:
                print("Yes")
            else:
                print("No")
