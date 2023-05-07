def main():
    n,m,k = map(int,input().split())
    f = [set() for _ in range(n)]
    b = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a,b = a-1,b-1
        f[a].add(b)
        f[b].add(a)
    for _ in range(k):
        c,d = map(int,input().split())
        c,d = c-1,d-1
        b[c].add(d)
        b[d].add(c)
    ans = [0]*n
    for i in range(n):
        ans[i] = len(f[i] - b[i] - {i}) - 1
    print(*ans)
