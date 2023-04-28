Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    print(max(min(R)-max(L)+1, 0))

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L_max = max(L)
    R_min = min(R)
    if R_min - L_max < 0:
        print(0)
    else:
        print(R_min - L_max + 1)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    l = [0] * (m + 1)
    r = [0] * (m + 1)
    for i in range(1, m + 1):
        l[i], r[i] = map(int, input().split())
    l = sorted(l)
    r = sorted(r)
    ans = 0
    for i in range(1, m + 1):
        ans += max(0, l[i] - r[i - 1])
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        li, ri = map(int, input().split())
        if li > l:
            l = li
        if ri < r:
            r = ri
    if l <= r:
        print(r - l + 1)
    else:
        print(0)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    l = 0
    r = n
    for i in range(m):
        li,ri = map(int,input().split())
        l = max(l,li)
        r = min(r,ri)
    print(max(r-l+1,0))

=======
Suggestion 6

def main():
    n,m=map(int,input().split())
    l=[0]*(n+1)
    r=[0]*(n+1)
    for i in range(m):
        a,b=map(int,input().split())
        l[a]+=1
        r[b]+=1
    for i in range(1,n+1):
        l[i]+=l[i-1]
    for i in range(n-1,0,-1):
        r[i]+=r[i+1]
    ans=0
    for i in range(1,n+1):
        if l[i-1]+r[i+1]==m:
            ans+=1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    l = [i[0] for i in lr]
    r = [i[1] for i in lr]
    print(max(0, min(r) - max(l) + 1))

=======
Suggestion 8

def get_ints():
    return [ int(s) for s in input().split() ]

N, M = get_ints()
Ls = []
Rs = []
for i in range(M):
    L, R = get_ints()
    Ls.append(L)
    Rs.append(R)

L = max(Ls)
R = min(Rs)
print(max(0, R - L + 1))

=======
Suggestion 9

def is_in_range(card, gate):
    return gate[0] <= card <= gate[1]
