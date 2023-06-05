Synthesizing 10/10 solutions

=======
Suggestion 1

def p127_d():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    bc = [list(map(int,input().split())) for _ in range(m)]
    bc.sort(key=lambda x:x[1],reverse=True)
    i = 0
    for b,c in bc:
        for _ in range(b):
            if a[i] < c:
                a[i] = c
                i += 1
                if i >= n:
                    break
            else:
                break
        if i >= n:
            break
    print(sum(a))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    # print(A)
    # print(BC)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        else:
            i += 1
    print(sum(A))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if i >= n or a[i] >= c:
                break
            a[i] = c
            i += 1
        else:
            continue
        break
    print(sum(a))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    BC = [list(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    ans = 0
    for j in range(M):
        if BC[j][0] + i < N:
            ans += BC[j][1] * BC[j][0]
            i += BC[j][0]
        else:
            ans += BC[j][1] * (N - i)
            break
    ans += sum(A[i:])
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if i >= N or c <= A[i]:
                break
            A[i] = c
            i += 1
    print(sum(A))

solve()

=======
Suggestion 6

def problems127_d():
    return None

=======
Suggestion 7

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    b=[]
    for i in range(m):
        b.append(list(map(int,input().split())))
    b.sort(key=lambda x:x[1],reverse=True)
    j=0
    for i in range(n):
        if j==m:
            break
        if a[i]<b[j][1]:
            a[i]=b[j][1]
            b[j][0]-=1
            if b[j][0]==0:
                j+=1
        else:
            break
    print(sum(a))

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
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
Suggestion 9

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
    c.sort(reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < c[j]:
            a[i] = c[j]
            j += 1
        i += 1
    print(sum(a))

=======
Suggestion 10

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
