Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    ab = [list(map(int,input().split())) for _ in range(m)]
    ans = 0
    for i in range(n):
        flag = True
        for j in range(m):
            if i+1 == ab[j][0] and h[i] <= h[ab[j][1]-1]:
                flag = False
                break
            elif i+1 == ab[j][1] and h[i] <= h[ab[j][0]-1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(n,m,h,a,b)
    ans = 0
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            ans += 1
        elif h[a[i]-1] < h[b[i]-1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    path = [list(map(int,input().split())) for _ in range(M)]
    good = [True] * N
    for i in range(M):
        if H[path[i][0]-1] <= H[path[i][1]-1]:
            good[path[i][0]-1] = False
        if H[path[i][1]-1] <= H[path[i][0]-1]:
            good[path[i][1]-1] = False
    print(good.count(True))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    good = [True] * n
    for i in range(m):
        if h[a[i]-1] <= h[b[i]-1]:
            good[a[i]-1] = False
        if h[b[i]-1] <= h[a[i]-1]:
            good[b[i]-1] = False
    print(good.count(True))

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            h[b[i]-1] = 0
        elif h[a[i]-1] < h[b[i]-1]:
            h[a[i]-1] = 0
        else:
            h[a[i]-1] = 0
            h[b[i]-1] = 0
    count = 0
    for i in range(n):
        if h[i] != 0:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    ab = [list(map(int,input().split())) for _ in range(m)]
    ans = 0
    for i in range(m):
        if h[ab[i][0]-1] > h[ab[i][1]-1]:
            ans += 1
        elif h[ab[i][0]-1] < h[ab[i][1]-1]:
            ans += 1
        else:
            pass
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M)
    print(H)
    print(A)
    print(B)
    cnt = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i + 1:
                if H[i] <= H[B[j] - 1]:
                    flag = False
            if B[j] == i + 1:
                if H[i] <= H[A[j] - 1]:
                    flag = False
        if flag:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def is_higher(h, i):
    for j in range(len(h)):
        if h[j] > h[i]:
            return False
    return True

=======
Suggestion 9

def problems166_c():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = list()
    B = list()
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if i+1 == A[j] and H[i] <= H[B[j]-1]:
                flag = False
            if i+1 == B[j] and H[i] <= H[A[j]-1]:
                flag = False
        if flag:
            ans += 1
    print(ans)

problems166_c()

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*n
    b = [0]*n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            b[i] = 0
        elif h[a[i]-1] < h[b[i]-1]:
            a[i] = 0
        else:
            a[i] = 0
            b[i] = 0
    a = list(set(a))
    b = list(set(b))
    print(len(a)+len(b))
