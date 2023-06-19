Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,q = map(int,input().spli

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    # print(N, Q)
    # print(type(N), type(Q))

    # 1. 创建一个字典，key是用户，value是关注用户的列表
    user_follow = {}
    for i in range(1, N+1):
        user_follow[i] = []

    # 2. 根据输入的操作，更新字典
    for i in range(Q):
        t, a, b = map(int, input().split())
        # print(t, a, b)
        if t == 1:
            user_follow[a].append(b)
        elif t == 2:
            user_follow[a].remove(b)
        elif t == 3:
            if b in user_follow[a] and a in user_follow[b]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 3

def follow(a,b):
    if a in follow_dic:
        if b in follow_dic[a]:
            return True
    return False

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def solve():
    N, Q = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(Q):
        t, a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    c = [0] * N
    for i in range(Q):
        if t == 1:
            c[a[i]] |= 1 << b[i]
        elif t == 2:
            c[a[i]] &= ~(1 << b[i])
        elif t == 3:
            if c[a[i]] & (1 << b[i]) and c[b[i]] & (1 << a[i]):
                print("Yes")
            else:
                print("No")
        else:
            assert(False)

=======
Suggestion 6

def main():
    n,q = input().split(" ")
    n = int(n)
    q = int(q)
    t = []
    a = []
    b = []
    for i in range(q):
        t_i,a_i,b_i = input().split(" ")
        t.append(int(t_i))
        a.append(int(a_i))
        b.append(int(b_i))
    #print(t)
    #print(a)
    #print(b)
    #print(n)
    #print(q)
    follow = []
    for i in range(n):
        follow.append([])
    for i in range(q):
        if t[i] == 1:
            follow[a[i]-1].append(b[i]-1)
        elif t[i] == 2:
            follow[a[i]-1].remove(b[i]-1)
        elif t[i] == 3:
            if a[i]-1 in follow[b[i]-1] and b[i]-1 in follow[a[i]-1]:
                print("Yes")
            else:
                print("No")
    #print(follow)

=======
Suggestion 7

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    follow = {}
    for i in range(1,n+1):
        follow[i] = []
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow[a].append(b)
        elif t == 2:
            follow[a].remove(b)
        elif t == 3:
            if b in follow[a] and a in follow[b]:
                print("Yes")
            else:
                print("No")
