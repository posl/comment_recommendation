Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]

    # 从大到小排序
    A.sort(reverse=True)
    BC.sort(key=lambda x: x[1], reverse=True)

    # 用于替换的数的索引
    i = 0
    # 用于替换的数的个数
    cnt = 0
    # 替换
    for b, c in BC:
        # 替换的数的索引
        while i < N and A[i] > c and cnt < b:
            A[i] = c
            i += 1
            cnt += 1

    # 输出
    print(sum(A))

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    bc = []
    for i in range(m):
        bc.append(list(map(int,input().split())))
    a.sort()
    bc.sort(key=lambda x:x[1],reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < bc[j][1]:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    print(sum(a))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    bc = []
    for i in range(m):
        bc.append(list(map(int,input().split())))
    bc.sort(key=lambda x:x[1],reverse=True)
    j = 0
    for i in range(n):
        if j < m:
            if bc[j][0] > 0:
                if a[i] < bc[j][1]:
                    a[i] = bc[j][1]
                    bc[j][0] -= 1
                else:
                    break
            else:
                j += 1
                i -= 1
        else:
            break
    print(sum(a))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    a.sort()
    a.reverse()
    a_i = 0
    c_i = 0
    while a_i < n and c_i < m:
        if a[a_i] >= c[c_i]:
            a_i += 1
        else:
            a[a_i] = c[c_i]
            b[c_i] -= 1
            if b[c_i] == 0:
                c_i += 1
    print(sum(a))

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i, j = 0, 0
    while i < n and j < m:
        if a[i] < bc[j][1]:
            a[i] = bc[j][1]
            bc[j] = (bc[j][0] - 1, bc[j][1])
            if bc[j][0] == 0:
                j += 1
        i += 1
    print(sum(a))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    C.sort()
    j = 0
    for i in range(N):
        if j < M and A[i] < C[M-j-1] and B[M-j-1] > 0:
            A[i] = C[M-j-1]
            B[M-j-1] -= 1
        else:
            j += 1
    print(sum(A))

=======
Suggestion 7

def solve(n, m, a, bc):
    a.sort(reverse=True)
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] > bc[j][1]:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    return sum(a)

=======
Suggestion 8

def solve(n, m, a, bc):
    a.sort(reverse=True)
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] >= bc[j][1]:
            i += 1
        else:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
            i += 1
    return sum(a)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    print(sum(A))

=======
Suggestion 10

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]

    # 按照A_i的大小顺序从大到小排序
    A.sort(reverse=True)

    # 降序排列BC
    BC.sort(key=lambda x: x[1], reverse=True)

    # 从大到小依次选取BC
    j = 0
    for i in range(N):
        if j < M and A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1

    # 输出结果
    print(sum(A))
