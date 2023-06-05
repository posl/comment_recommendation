Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n,m = map(int,input().split())
    a = [0 for _ in range(n+1)]
    for _ in range(m):
        l,r = map(int,input().split())
        a[l-1] += 1
        a[r] -= 1
    for i in range(n):
        a[i+1] += a[i]
    print(a.count(m))

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if N == 1:
        print(1)
    else:
        if L[-1] > R[0]:
            print(0)
        else:
            print(R[0]-L[-1]+1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[-1] <= R[0]:
        print(R[0] - L[-1] + 1)
    else:
        print(0)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()

    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)

=======
Suggestion 5

def solve():
    N,M = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L = max(L)
    R = min(R)
    if L <= R:
        print(R-L+1)
    else:
        print(0)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i], R[i] = map(int, input().split())

    L.sort()
    R.sort()
    ans = 0
    for i in range(1, M):
        ans += L[i] - R[i-1] - 1
    print(ans + N - R[M-1] + L[0] - 1)

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)
    l.sort()
    r.sort()
    print(max(0, min(r) - max(l) + 1))

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        l[a - 1] += 1
        l[b] -= 1
    for i in range(n):
        l[i + 1] += l[i]
    print(l.count(m))

=======
Suggestion 9

def main():
    #N张ID卡，M个闸门
    N, M = map(int, input().split())
    #N张ID卡可以通过的闸门的范围
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    #每张ID卡可以通过的闸门的数量
    num = [0] * (N+1)
    for i in range(M):
        num[L[i]-1] += 1
        num[R[i]] -= 1
    #前缀和
    for i in range(1, N):
        num[i] += num[i-1]
    #通过所有闸门的ID卡数量
    ans = 0
    for i in range(N):
        if num[i] == M:
            ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)
