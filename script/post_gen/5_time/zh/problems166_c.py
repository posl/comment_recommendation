Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1

    is_good = [True] * n
    for i in range(m):
        if h[a[i]] <= h[b[i]]:
            is_good[a[i]] = False
        if h[b[i]] <= h[a[i]]:
            is_good[b[i]] = False

    print(is_good.count(True))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    H.insert(0, 0)
    #print(H)
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print(AB)

    result = [1] * (N+1)
    for i in range(M):
        if H[AB[i][0]] < H[AB[i][1]]:
            result[AB[i][0]] = 0
        elif H[AB[i][0]] > H[AB[i][1]]:
            result[AB[i][1]] = 0
        elif H[AB[i][0]] == H[AB[i][1]]:
            result[AB[i][0]] = 0
            result[AB[i][1]] = 0
    print(sum(result))

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    # print(N,M)
    # print(H)
    # print(A)
    # print(B)
    # print(H)
    # print(A)
    # print(B)
    # print(H[0])
    # print(H[A[0]-1])
    # print(H[B[0]-1])
    # print(H[A[0]-1] > H[B[0]-1])
    # print(H[0] > H[A[0]-1])
    # print(H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] and H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])

    # print(H[0] > H[A[0]-1] or H[0] > H[B[0]-1])
    # print(H[1] > H[A[1]-1] or H[1] > H[B[

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    ab = [list(map(int,input().split())) for _ in range(m)]
    ans = 0
    for i in range(n):
        flag = True
        for j in range(m):
            if i+1 == ab[j][0]:
                if h[i] <= h[ab[j][1]-1]:
                    flag = False
            elif i+1 == ab[j][1]:
                if h[i] <= h[ab[j][0]-1]:
                    flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def problems166_c():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M, H, AB)
    ans = N
    for i in range(M):
        if H[AB[i][0]-1] >= H[AB[i][1]-1]:
            ans -= 1
        if H[AB[i][0]-1] <= H[AB[i][1]-1]:
            ans -= 1
    print(ans)

problems166_c()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    ans = 0
    for i in range(N):
        for j in edges[i]:
            if H[i] <= H[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = []
    b = []
    for i in range(m):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])

    # print(n, m)
    # print(h)
    # print(a)
    # print(b)

    result = [1] * n
    for i in range(m):
        if h[a[i]-1] <= h[b[i]-1]:
            result[a[i]-1] = 0
        if h[b[i]-1] <= h[a[i]-1]:
            result[b[i]-1] = 0

    print(sum(result))

=======
Suggestion 8

def main():
    print("hello world")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M, H, A, B)
    #print(H[0:3])
    #print(A[0:3])
    #print(B[0:3])
    #print(H[A[0]-1], H[B[0]-1])
    #print(H[A[1]-1], H[B[1]-1])
    #print(H[A[2]-1], H[B[2]-1])
    #print(H[A[3]-1], H[B[3]-1])
    #print(H[A[4]-1], H[B[4]-1])
    #print(H[A[5]-1], H[B[5]-1])
    #print(H[0], H[2])
    #print(H[3], H[1])
    #print(H[3], H[2])
    #print(H[3], H[5])
    #print(H[3], H[5])
    #print(H[3], H[5])
    #print(H[0] > H[2])
    #print(H[3] > H[1])
    #print(H[3] > H[2])
    #print(H[3] > H[5])
    #print(H[3] > H[5])
    #print(H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[1] or H[3] > H[2] or H[3] > H[5] or H[3] > H[5] or H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[2] or H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[2] or H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[2] or H[3] > H[5])

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)

    #print(n,m,h,a,b)

    #创建一个n*n的矩阵，用于存储各个节点之间的关系
    #0表示不通，1表示通
    #c = [[0 for i in range(n)] for j in range(n)]
    c = [[0]*n for i in range(n)]
    for i in range(m):
        c[a[i]-1][b[i]-1] = 1
        c[b[i]-1][a[i]-1] = 1
    #print(c)

    #遍历每个节点，判断是否满足条件
    #如果满足条件，则该节点为好的观测站
    #如果不满足条件，则该节点不是好的观测站

    #计算每个节点的海拔高度
    #找到所有节点中的最大海拔高度
    #maxh = max(h)
    #print(maxh)
    #print(h)
    #print(max(h))

    #创建一个空列表，用于存储好的观测站
    g = []
    for i in range(n):
        #print(i)
        #print(h[i])
        #print(max(h))
        #如果当前节点的海拔高度大于所有节点中的最大海拔高度
        #则该节点为好的观测站
        #如果当前节点的海拔高度小于所有节点中的最大海拔高度
        #则该节点不是好的观测站
        if h[i] >= max(h):
            #print('good')
            g.append(i)
        else:
            #print('bad')
            pass
    #print(g)
    #print(len(g))

    #判断好的观测站的个数
    #如果只有一个好的观测站，那
