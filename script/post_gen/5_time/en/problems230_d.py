Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    l = 0
    r = 0
    while l < N:
        if L[l] <= R[r]:
            ans += 1
            l += 1
        else:
            r += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        ans += 1
        if i > 0:
            if L[i] - R[i-1] < D:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        ans += 1
        if i == N - 1:
            break
        if L[i + 1] - R[i] > D:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    l.sort()
    r.sort()
    i = 0
    j = 0
    ans = 0
    while i < n:
        if l[i] < r[j]:
            ans += 1
            i += 1
        else:
            j += 1
            i += 1
    print(ans)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort(key=lambda x: x[0])
    #print(walls)
    ans = 0
    for i in range(N):
        L, R = walls[i]
        #print(L, R)
        if L > D:
            ans += 1
        if R > D:
            ans += 1
            D = L
        else:
            D = min(D, L)
        #print(ans, D)
    if D > 0:
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        l, r = map(int, input().split())
        walls.append((l, r))
    walls.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        l, r = walls[i]
        if l <= ans:
            ans = ans - ans % D + r
        else:
            ans = ans - ans % D + l + D - 1
    print(ans)

=======
Suggestion 7

def main():
    n,d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        x,y = map(int, input().split())
        l.append(x)
        r.append(y)
    l.sort()
    r.sort()
    ans = 0
    for i in range(n):
        ans += 1
        if i != n-1:
            if l[i+1] - r[i] < d:
                ans -= 1
    print(ans)

=======
Suggestion 8

def solve():
    n, d = map(int, input().split())
    a = [0] * n
    for i in range(n):
        l, r = map(int, input().split())
        a[i] = (l, r)
    a.sort()
    ans = 0
    for i in range(n):
        l, r = a[i]
        while l <= r:
            ans += 1
            l += d
    print(ans)

solve()

=======
Suggestion 9

def solve(N,D,LR):
    LR.sort()
    L,R = [],[]
    for l,r in LR:
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    L.append(10**9+1)
    R.append(10**9+1)
    ans = 0
    l,r = 0,0
    for i in range(1,N+1):
        while L[l] <= i:
            l += 1
        while R[r] <= i:
            r += 1
        ans = max(ans,r-l)
    return ans
N,D = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(N)]
print(solve(N,D,LR))

=======
Suggestion 10

def solve(N,D,LR):
    LR.sort()
    LR.append([10**9+1,10**9+1])
    #print(LR)
    ans = 0
    for i in range(N):
        l,r = LR[i]
        nl,nr = LR[i+1]
        #print(l,r,nl,nr)
        if l==r:
            continue
        if l+D<=r:
            continue
        if l+D<=nl:
            continue
        if l+D>nr:
            ans += 1
            continue
        if l+D<=nr:
            ans += 1
            LR[i+1][0] = l+D
            continue
    return ans
