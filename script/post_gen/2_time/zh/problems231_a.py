Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,d = map(int,input().split())
    l = []
    r = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    ans = 0
    for i in range(n):
        ans += 1
        if i == n-1:
            break
        if l[i+1] - r[i] >= d:
            continue
        if l[i+1] - l[i] >= d:
            continue
        if r[i+1] - l[i] >= d:
            continue
        ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    i = 0
    j = 0
    ans = 0
    while i < n:
        if l[i] <= r[j]:
            i += 1
            ans += 1
        else:
            j += 1
            ans -= 1
    print(ans)

=======
Suggestion 4

def solve():
    N, D = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(N)]
    LRs.sort()
    LRs.append([10**9+1, 10**9+1])
    ans = 0
    p = 0
    for i in range(N):
        L, R = LRs[i]
        while p < N and LRs[p][0] <= R:
            p += 1
        ans += max(0, p-i-1)
    print(ans)

solve()

=======
Suggestion 5

def main():
    N,D=map(int,input().split())
    L=[]
    R=[]
    for i in range(N):
        l,r=map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans=0
    i=0
    j=0
    while i<N:
        if L[i]<=R[j]:
            ans+=1
            i+=1
        else:
            ans-=1
            j+=1
        if ans>D:
            print("NO")
            return
    print("YES")

=======
Suggestion 6

def solve():
    #解题算法
    return

=======
Suggestion 7

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
    i = 0
    j = 0
    now = 0
    while i < N:
        if L[i] <= R[j]:
            now += 1
            i += 1
        else:
            now -= 1
            j += 1
        ans = max(ans, now)
    print(ans)

=======
Suggestion 8

def main():
    n,d = map(int,input().split())
    l = []
    r = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    ans = 0
    i = 0
    j = 0
    while i < n:
        if l[i] <= r[j]:
            ans += 1
            i += 1
        else:
            ans -= 1
            j += 1
    print(ans)
