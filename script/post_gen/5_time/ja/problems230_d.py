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
    R.so

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    Ls = []
    Rs = []
    for i in range(N):
        L, R = map(int, input().split())
        Ls.append(L)
        Rs.append(R)
    Ls.sort()
    Rs.sort()
    ans = 0
    for i in range(N):
        ans += 1
        if Rs[i] - Ls[i] >= D:
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
    count = 0
    for i in range(N):
        if L[i] - R[i] > 0:
            count += 1
        else:
            count -= 1
        if count > ans:
            ans = count
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        Li, Ri = map(int, input().split())
        L.append(Li)
        R.append(Ri)
    L.sort()
    R.sort()
    ans = 0
    i = 0
    j = 0
    while i < N:
        if L[i] <= R[j]:
            i += 1
        else:
            j += 1
        if j - i > ans:
            ans = j - i
    print(ans)

=======
Suggestion 5

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
        if i == 0:
            ans += 1
        if i == N-1:
            ans += 1
        ans += (L[i] - R[i-1] - 1) // D
    print(ans)

=======
Suggestion 6

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
    L = L[::-1]
    R = R[::-1]
    ans = 0
    l = 0
    r = 0
    while l < N and r < N:
        if L[l] <= R[r]:
            ans += 1
            l += 1
        else:
            ans -= 1
            r += 1
    print(ans)

=======
Suggestion 7

def main():
    n,d = map(int,input().split())
    l = []
    r = []
    for i in range(n):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    ans = 1
    tmp = 0
    for i in range(n):
        tmp += 1
        if i == n-1:
            break
        if l[i+1] - r[i] > d:
            ans += 1
            tmp = 0
    print(ans)

=======
Suggestion 8

def solve(N, D, LRs):
    LRs.sort()
    ans = 1
    for i in range(N-1):
        if LRs[i+1][0] - LRs[i][1] >= D:
            ans += 1
    return ans

N, D = map(int, input().split())
LRs = [list(map(int, input().split())) for _ in range(N)]
print(solve(N, D, LRs))

=======
Suggestion 9

def solve():
    pass

=======
Suggestion 10

def main():
    n, d = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(n)]
    lrs.sort(key=lambda x: x[0])
    r = 0
    ans = 0
    for l, r in lrs:
        if r - l + 1 > d:
            ans += (r - l) // d
    print(ans)
