Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [[int(i) for i in input().split()] for _ in range(M)]
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

main()

=======
Suggestion 2

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    # 解决
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if i >= n or a[i] >= c:
                break
            a[i] = c
            i += 1
    print(sum(a))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    bc = [list(map(int,input().split())) for _ in range(m)]
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
    print(sum(a))

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = []
    for i in range(M):
        BC.append(list(map(int,input().split())))
    A.sort(reverse=True)
    BC.sort(key=lambda x: x[1],reverse=True)
    i = 0
    j = 0
    while i<N and j<M:
        if A[i]<BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0]==0:
                j += 1
            i += 1
        else:
            break
    print(sum(A))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for j in range(b):
            if i < n and a[i] < c:
                a[i] = c
                i += 1
            else:
                break
    print(sum(a))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    idx = 0
    for i in range(m):
        for j in range(bc[i][0]):
            if idx < n and a[idx] < bc[i][1]:
                a[idx] = bc[i][1]
                idx += 1
            else:
                break
    print(sum(a))

=======
Suggestion 7

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    # 从大到小排序
    a.sort(reverse=True)
    bc.sort(key=lambda x: x[1], reverse=True)
    # 从大到小取得最大值
    ans = 0
    j = 0
    for i in range(n):
        if j < m and a[i] < bc[j][1]:
            ans += bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    bc = [list(map(int,input().split())) for _ in range(m)]
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
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    bc = [list(map(int,input().split())) for i in range(m)]
    a.sort()
    bc.sort(key=lambda x:x[1],reverse=True)
    i = 0
    for b,c in bc:
        while b>0 and i<n and a[i]<c:
            a[i] = c
            i += 1
            b -= 1
    print(sum(a))

=======
Suggestion 10

def problems127_d():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1],reverse=True)
    i = 0
    j = 0
    while j<M and i<N and BC[j][1]>A[i]:
        A[i] = BC[j][1]
        BC[j][0] -= 1
        if BC[j][0]==0:
            j += 1
        i += 1
    print(sum(A))
