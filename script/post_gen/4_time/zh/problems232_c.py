Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    print(A)
    print(B)
    print(C)
    print(D)

=======
Suggestion 2

def main():
    n,m=map(int,input().split())
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x,y=map(int,input().split())
        c.append(x)
        d.append(y)
    if a==c and b==d:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        Ai,Bi = map(int,input().split())
        A.append(Ai)
        B.append(Bi)
    for i in range(M):
        Ci,Di = map(int,input().split())
        C.append(Ci)
        D.append(Di)
    #print(A,B,C,D)
    #print(N,M)
    #print(A[0],B[0],C[0],D[0])

    #print(A[0],B[0],C[0],D[0])
    #print(A[1],B[1],C[1],D[1])
    #print(A[2],B[2],C[2],D[2])
    #print(A[3],B[3],C[3],D[3])

    #print(A[0],B[0],C[0],D[0])
    #print(A[1],B[1],C[1],D[1])
    #print(A[2],B[2],C[2],D[2])
    #print(A[3],B[3],C[3],D[3])
    #print(A[4],B[4],C[4],D[4])
    #print(A[5],B[5],C[5],D[5])

    #print(A[0],B[0],C[0],D[0])
    #print(A[1],B[1],C[1],D[1])
    #print(A[2],B[2],C[2],D[2])
    #print(A[3],B[3],C[3],D[3])
    #print(A[4],B[4],C[4],D[4])
    #print(A[5],B[5],C[5],D[5])
    #print(A[6],B[6],C[6],D[6])
    #print(A[7],B[7],C[7],D[7])
    #print(A[8],B[8],C[8],D[8])
    #print(A[9],B[9],C[9],D[9

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(M):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(M):
        x,y = map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(1,N+1):
        if i not in a:
            a.append(i)
            b.append(i)
        if i not in c:
            c.append(i)
            d.append(i)
    for i in range(N):
        for j in range(i+1,N):
            if a[i] == a[j] and b[i] == b[j]:
                if c[i] != c[j] or d[i] != d[j]:
                    print('No')
                    exit()
            if a[i] == b[j] and b[i] == a[j]:
                if c[i] != d[j] or d[i] != c[j]:
                    print('No')
                    exit()
    print('Yes')
    exit()

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    # 读入数据
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    b = [list(map(int, input().split())) for _ in range(m)]

    # 判断是否有相同的形状
    # 1. 先判断是否有相同的绳子
    # 2. 再判断是否有相同的球
    # 3. 再判断是否有相同的绳子
    # 4. 再判断是否有相同的球
    # 5. 依次类推
    # 6. 如果都没有相同的球和绳子，则两个玩具有相同的形状
    for i in range(1 << n):
        # 1. 先判断是否有相同的绳子
        # 2. 再判断是否有相同的球
        # 3. 再判断是否有相同的绳子
        # 4. 再判断是否有相同的球
        # 5. 依次类推
        # 6. 如果都没有相同的球和绳子，则两个玩具有相同的形状
        # 1. 先判断是否有相同的绳子
        # 2. 再判断是否有相同的球
        # 3. 再判断是否有相同的绳子
        # 4. 再判断是否有相同的球
        # 5. 依次类推
        # 6. 如果都没有相同的球和绳子，则两个玩具有相同的形状
        # 1. 先判断是否有相同的绳子
        # 2. 再判断是否有相同的球
        # 3. 再判断是否有相同的绳子
        # 4. 再判断是否有相同的球
        # 5. 依次类推
        # 6. 如果都没有相同

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    p = list(range(n))
    def root(x):
        if p[x] != x: p[x] = root(p[x])
        return p[x]
    for i in range(m):
        a[i][0] -= 1
        a[i][1] -= 1
        c[i][0] -= 1
        c[i][1] -= 1
    for i in range(m):
        p[root(a[i][0])] = root(a[i][1])
    q = list(range(n))
    for i in range(m):
        q[root(c[i][0])] = root(c[i][1])
    print("Yes" if p == q else "No")

solve()

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(2 ** N):
        P = []
        for j in range(N):
            if (i >> j) & 1:
                P.append(j + 1)
        if len(P) != N:
            continue
        flag = True
        for j in range(M):
            if ((A[j] in P) and (B[j] in P)) or ((not (A[j] in P)) and (not (B[j] in P))):
                if ((C[j] in P) and (D[j] in P)) or ((not (C[j] in P)) and (not (D[j] in P))):
                    continue
                else:
                    flag = False
                    break
            else:
                if ((C[j] in P) and (D[j] in P)) or ((not (C[j] in P)) and (not (D[j] in P))):
                    flag = False
                    break
                else:
                    continue
        if flag:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def solve():
    pass
