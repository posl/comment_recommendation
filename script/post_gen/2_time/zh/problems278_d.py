Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    users = {i: set() for i in range(1, N+1)}
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            users[A].add(B)
        elif T == 2:
            users[A].discard(B)
        else:
            print("Yes" if A in users[B] and B in users[A] else "No")

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    follow = []
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow.append((A, B))
        elif T == 2:
            follow.remove((A, B))
        else:
            if (A, B) in follow and (B, A) in follow:
                print("Yes")
            else:
                print("No")

=======
Suggestion 3

def main():
    n,q = map(int,input().split())
    follow = {}
    for i in range(1,n+1):
        follow[i] = set()
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[a].discard(b)
        elif t == 3:
            if b in follow[a] and a in follow[b]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 4

def main():
    # 读取标准输入
    N, Q = map(int, input().split())
    # print(N, Q)
    # print(type(N), type(Q))
    # 生成一个N*N的二维列表
    matrix = [[0 for i in range(N)] for j in range(N)]
    # print(matrix)
    # print(type(matrix))
    # 读取操作
    for i in range(Q):
        T, A, B = map(int, input().split())
        # print(T, A, B)
        # print(type(T), type(A), type(B))
        if T == 1:
            # A关注B
            matrix[A - 1][B - 1] = 1
        elif T == 2:
            # A取消关注B
            matrix[A - 1][B - 1] = 0
        elif T == 3:
            # 判断A和B是否互相关注
            if matrix[A - 1][B - 1] == 1 and matrix[B - 1][A - 1] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def follow(followers, followings, a, b):
    if a == b:
        return False
    if b in followings[a]:
        return True
    return False

=======
Suggestion 7

def find_father(fathers, x):
    if fathers[x] == x:
        return x
    else:
        fathers[x] = find_father(fathers, fathers[x])
        return fathers[x]

=======
Suggestion 8

def follow(a,b):
    if a in follow_dict.keys():
        follow_dict[a].append(b)
    else:
        follow_dict[a] = [b]
    if b in followed_dict.keys():
        followed_dict[b].append(a)
    else:
        followed_dict[b] = [a]

=======
Suggestion 9

def main():
    n,q = map(int,input().split())
    t = []
    a = []
    b = []
    for i in range(q):
        t1,a1,b1 = map(int,input().split())
        t.append(t1)
        a.append(a1)
        b.append(b1)
    for i in range(q):
        if t[i] == 1:
            print("No")
        elif t[i] == 2:
            print("No")
        else:
            if a[i] == b[i]:
                print("Yes")
            else:
                print("No")
