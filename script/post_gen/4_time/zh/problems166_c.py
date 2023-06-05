Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [li

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    #print(N,M,H,A,B)
    #print(H)
    #print(A)
    #print(B)
    #print(H[1])
    #print(H[3])
    #print(A[1])

=======
Suggestion 3

def main():
    # 读入数据
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    # 从1开始编号
    h.insert(0, 0)
    # 用set存储连接关系
    con = set()
    for i in range(m):
        a, b = map(int, input().split())
        con.add((a, b))
        con.add((b, a))

    # 计算好的观测站
    ans = 0
    for i in range(1, n + 1):
        # 遍历所有观测站，如果当前观测站的海拔高于其它观测站，则它是好的
        for j in range(1, n + 1):
            if h[i] <= h[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    #input
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())

    #init
    good = [1]*n

    #solve
    for i in range(m):
        if h[a[i]-1] <= h[b[i]-1]:
            good[a[i]-1] = 0
        if h[b[i]-1] <= h[a[i]-1]:
            good[b[i]-1] = 0

    #output
    print(sum(good))

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    # 读取输入
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    # print("N,M,H:",N,M,H)
    # 创建一个数组，用来存储每个观测站的高度
    # 从1号观测站开始，到N号观测站结束
    # 由于python从0开始，所以需要N+1个元素
    # 为了方便计算，第0个元素不使用
    H = [0] + H
    # print("H",H)
    # 创建一个数组，用来存储每个观测站的好坏
    # 从1号观测站开始，到N号观测站结束
    # 由于python从0开始，所以需要N+1个元素
    # 为了方便计算，第0个元素不使用
    good = [0] * (N + 1)
    # print("good",good)
    # 创建一个数组，用来存储每个观测站的连接关系
    # 从1号观测站开始，到N号观测站结束
    # 由于python从0开始，所以需要N+1个元素
    # 为了方便计算，第0个元素不使用
    # 这个数组是一个二维数组，每个元素是一个列表，用来存储观测站之间的连接关系
    # 比如，[[], [3], [3], [1, 2, 4], [2, 3, 5, 6], [4], [4]]
    # 表示1号观测站可以通过3号观测站到达，2号观测站可以通过3号观测站到达，3号观测站可以通过1、2、4号观测站到达，4号观测站可以通过2、3、5、6号

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(H)
    # print(ab)

    good = [True] * N
    for a, b in ab:
        if H[a-1] <= H[b-1]:
            good[a-1] = False
        if H[b-1] <= H[a-1]:
            good[b-1] = False

    print(good.count(True))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(H)
    #print(A)
    #print(B)
    #print("----------")
    #print(N, M, H, A, B)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            #print(i, j)
            #print(H[A[j]-1], H[B[j]-1])
            if H[A[j]-1] >= H[B[j]-1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    # 良い天気台の数
    ans = n
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for a, b in ab:
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    for i in range(n):
        for j in adj[i]:
            if h[i] <= h[j]:
                ans -= 1
                break

    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 1. 1 から N までの各頂点について、その頂点から到達可能な頂点のうち、最大の H の値を求める
    # 2. 1 から N までの各頂点について、その頂点の H の値が、その頂点から到達可能な頂点のうち、最大の H の値以下であるとき、その頂点は良い頂点である

    # 1. 1 から N までの各頂点について、その頂点から到達可能な頂点のうち、最大の H の値を求める
    max_h = [0] * N
    for a, b in AB:
        max_h[a - 1] = max(max_h[a - 1], H[b - 1])
        max_h[b - 1] = max(max_h[b - 1], H[a - 1])

    # 2. 1 から N までの各頂点について、その頂点の H の値が、その頂点から到達可能な頂点のうち、最大の H の値以下であるとき、その頂点は良い頂点である
    ans = 0
    for i in range(N):
        if H[i] <= max_h[i]:
            ans += 1

    print(ans)
