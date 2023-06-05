def solve():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for l,r in query:
        ans = 0
        for i in range(m):
            if l <= i+1 <= r:
                continue
            for j in range(n):
                if x[i] >= wv[j][0]:
                    ans = max(ans,wv[j][1])
        print(ans)
