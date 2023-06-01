Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, m, a, b, c):
    bc = []
    for i in range(m):
        bc.append((b[i], c[i]))
    bc.sort(key=lambda x: x[1], reverse=True)
    # print(bc)
    i = 0
    ans = 0
    for k in range(n):
        if i < m and bc[i][0] > 0:
            ans += bc[i][1]
            bc[i] = (bc[i][0] - 1, bc[i][1])
        else:
            ans += a[k]
        # print(ans)
        while i < m and bc[i][0] == 0:
            i += 1
    return ans

=======
Suggestion 2

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    c = []
    for i in range(m):
        bi,ci = map(int,input().split())
        b.append(bi)
        c.append(ci)
    b = b[::-1]
    c = c[::-1]
    index = 0
    ans = 0
    for i in range(n):
        if index < m and a[i] < c[index]:
            ans += c[index]
            b[index] -= 1
            if b[index] == 0:
                index += 1
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 3

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    b=[]
    c=[]
    for i in range(m):
        bi,ci=map(int,input().split())
        b.append(bi)
        c.append(ci)
    b.sort()
    c.sort()
    sum=0
    for i in range(m):
        if(a[n-1]>c[m-i-1]):
            sum+=a[n-1]
            n-=1
        else:
            sum+=c[m-i-1]
            if(b[m-i-1]>n):
                n=0
            else:
                n-=b[m-i-1]
    for i in range(n):
        sum+=a[i]
    print(sum)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]

    A.sort(reverse=True)
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

    print(sum(A))

main()

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [list(map(int, input().split())) for i in range(m)]
    a.sort(reverse=True)
    b.sort(key=lambda x:x[1], reverse=True)
    j = 0
    for i in range(n):
        if j < m and a[i] < b[j][1]:
            a[i] = b[j][1]
            b[j][0] -= 1
            if b[j][0] == 0:
                j += 1
    print(sum(a))

=======
Suggestion 6

def main():
    # 读入数据
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    bc = []
    for i in range(m):
        bc.append(list(map(int,input().split())))
    # 操作
    a.sort()
    bc.sort(key=lambda x:x[1],reverse=True)
    idx = 0
    for i in range(m):
        for j in range(bc[i][0]):
            if idx >= n:
                break
            if a[idx] < bc[i][1]:
                a[idx] = bc[i][1]
                idx += 1
            else:
                break
    # 答案
    print(sum(a))

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    b = []
    c = []
    for i in range(m):
        b_i,c_i = map(int,input().split())
        b.append(b_i)
        c.append(c_i)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < c[j]:
            a[i] = c[j]
            b[j] -= 1
            if b[j] == 0:
                j += 1
        i += 1
    print(sum(a))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append([b, c])
    bc.sort(key=lambda x: x[1], reverse=True)
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

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        b1,c1 = map(int,input().split())
        b.append(b1)
        c.append(c1)
    b = [b[i] for i in range(m) if c[i] > a[b[i]-1]]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+

=======
Suggestion 10

def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]

    # 贪心算法
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)

    p = 0
    for b, c in bc:
        for _ in range(b):
            if p >= n or a[p] >= c:
                break
            a[p] = c
            p += 1

    print(sum(a))
