Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    # 读取输入
    n, m = map(int, input().split())
    # 用来记录每个人的左右边界
    l, r = [0] * n, [0] * n
    # 用来记录每个人的右边界的最小值和左边界的最大值
    min_right, max_left = n, 0
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        # 更新左右边界
        l[b] = max(l[b], a + 1)
        r[a] = max(r[a], b + 1)
        # 更新右边界的最小值和左边界的最大值
        min_right = min(min_right, b)
        max_left = max(max_left, a)
    # 用来记录当前人的左边界的最大值
    max_l = 0
    for i in range(n):
        # 更新当前人的左边界的最大值
        max_l = max(max_l, l[i])
        # 如果当前人的左边界的最大值大于右边界的最小值，说明不满足条件
        if max_l > min_right:
            print("No")
            return
        # 如果当前人的右边界的最小值大于左边界的最大值，说明不满足条件
        if r[i] > max_left:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(m):
        x, y = map(int, input().split())
        a[x] += 1
        a[y] += 1
    for i in range(1, n + 1):
        if a[i] % 2 == 1:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def solve():
    # 读取输入
    n, m = map(int, input().split())
    # 初始化并查集
    uf = UnionFind(n)
    # 读取条件
    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a - 1, b - 1)
    # 判断是否满足条件
    print("Yes" if uf.all_same() else "No")
    return

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        edge[A-1].append(B-1)
        edge[B-1].append(A-1)

    #print(edge)
    #print(len(edge[0]))
    #print(len(edge[1]))
    #print(len(edge[2]))
    #print(len(edge[3]))
    for i in range(N):
        if len(edge[i]) % 2 == 1:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def solve(n, m, a, b):
    if m == 0:
        return True
    for i in range(m):
        if a[i] == 1:
            if b[i] == 2:
                return False
        elif a[i] == n:
            if b[i] == n-1:
                return False
        elif a[i] == b[i]-1:
            if b[i] == a[i]+1:
                return False
    return True

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    AB.sort(key=lambda x:x[1])
    right = 0
    ans = 0
    for a,b in AB:
        if right < a:
            ans += 1
            right = b - 1
    print('Yes' if ans == 1 else 'No')

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    A = [0]*m
    B = [0]*m
    for i in range(m):
        A[i],B[i] = map(int,input().split())
    print(A,B)
    print(n,m)

=======
Suggestion 8

def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[-1] < B[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    if a[0] < b[0] and b[0] < a[1] and a[1] < b[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a = sorted(a)
    b = sorted(b)
    if a[0] > b[-1]:
        print('No')
    else:
        print('Yes')
