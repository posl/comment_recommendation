Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    good = [True] * N
    for i in range(M):
        if H[A[i] - 1] <= H[B[i] - 1]:
            good[A[i] - 1] = False
        if H[B[i] - 1] <= H[A[i] - 1]:
            good[B[i] - 1] = False

    print(sum(good))

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n, m = map(int, input().split())

    h = list(map(int, input().split()))

    ab = [list(map(int, input().split())) for _ in range(m)]

    good = [True] * n

    for a, b in ab:
        if h[a - 1] < h[b - 1]:
            good[a - 1] = False
        elif h[a - 1] > h[b - 1]:
            good[b - 1] = False
        else:
            good[a - 1] = False
            good[b - 1] = False

    print(sum(good))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(N,M,H,AB)
    #N = 6
    #M = 5
    #H = [8, 6, 9, 1, 2, 1]
    #AB = [[1, 3], [4, 2], [4, 3], [4, 6], [4, 6]]
    #print(N,M,H,AB)
    #print(N,M,H,AB)
    #N = 4
    #M = 3
    #H = [1, 2, 3, 4]
    #AB = [[1, 3], [2, 3], [2, 4]]
    #print(N,M,H,AB)
    #print(N,M,H,AB)
    #N = 4
    #M = 3
    #H = [1, 2, 3, 4]
    #AB = [[1, 3], [2, 3], [2, 4]]
    #print(N,M,H,AB)

    #N = 4
    #M = 3
    #H = [1, 2, 3, 4]
    #AB = [[1, 3], [2, 3], [2, 4]]
    #print(N,M,H,AB)
    #N = 4
    #M = 3
    #H = [1, 2, 3, 4]
    #AB = [[1, 3], [2, 3], [2, 4]]
    #print(N,M,H,AB)

    #N = 4
    #M = 3
    #H = [1, 2, 3, 4]
    #AB = [[1, 3], [2, 3], [2, 4]]
    #print(N,M,H,AB)

    #N = 4
    #M = 3
    #H = [1, 2, 3, 4]
    #AB = [[1, 3], [2, 3],

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        flag = True
        for j in range(m):
            if i+1 == a[j] or i+1 == b[j]:
                continue
            if h[i] <= h[a[j]-1] or h[i] <= h[b[j]-1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    ans = 0
    for i in range(n):
        flag = True
        for edge in edges:
            if i+1 in edge:
                if h[i] <= h[edge[0]-1] or h[i] <= h[edge[1]-1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    #输入
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        #print(a,b)
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #计算
    #定义一个列表用来存储是否是好的观测站
    good = [True]*N
    #print(good)
    #遍历所有的道路
    for i in range(M):
        #print(i)
        #print(H[A[i]-1],H[B[i]-1])
        #print(A[i],B[i])
        #print(good[A[i]-1],good[B[i]-1])
        #print(good[A[i]-1] and good[B[i]-1])
        #print(H[A[i]-1] <= H[B[i]-1])
        #print(H[A[i]-1] >= H[B[i]-1])
        #print(H[A[i]-1] <= H[B[i]-1] and H[A[i]-1] >= H[B[i]-1])
        #print(good[A[i]-1] and good[B[i]-1] and H[A[i]-1] <= H[B[i]-1] and H[A[i]-1] >= H[B[i]-1])
        if good[A[i]-1] and good[B[i]-1] and H[A[i]-1] <= H[B[i]-1] and H[A[i]-1] >= H[B[i]-1]:
            good[A[i]-1] = False
            good[B[i]-1] = False
            #print(good)
        elif good[A[i]-1] and H[A[i]-1] >= H[B[i]-1]:
            good[A[i]-1] = False
            #print(good)
        elif good[B[i]-1] and H[A[i]-1] <= H[B[i]-1]:
            good[B[i]-1] = False
            #print(good)
    #print(good)
    #输出
    print(good.count(True))

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    AB = [list(map(int,input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if AB[j][0] == i+1:
                if H[i] <= H[AB[j][1]-1]:
                    flag = False
            elif AB[j][1] == i+1:
                if H[i] <= H[AB[j][0]-1]:
                    flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    count = 0
    for i in range(N):
        flag = 0
        for j in range(M):
            if i+1 == A[j]:
                if H[i] <= H[B[j]-1]:
                    flag = 1
                    break
            elif i+1 == B[j]:
                if H[i] <= H[A[j]-1]:
                    flag = 1
                    break
        if flag == 0:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print(n,m)
    print(h)
    print(a)
    print(b)
    #print(h[a[0]-1])
    #print(h[b[0]-1])
    #print(h[a[1]-1])
    #print(h[b[1]-1])
    #print(h[a[2]-1])
    #print(h[b[2]-1])

    #print(h[a[0]-1] > h[b[0]-1])
    #print(h[a[1]-1] > h[b[1]-1])
    #print(h[a[2]-1] > h[b[2]-1])
    #print(h[a[0]-1] > h[b[0]-1] and h[a[1]-1] > h[b[1]-1] and h[a[2]-1] > h[b[2]-1])
    #print(h[0] > h[1])

    count = 0
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            count += 1
    print(count)
