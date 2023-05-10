def main():
    n,k = map(int,input().split())
    td = [list(map(int,input().split())) for _ in range(n)]
    td.sort(key=lambda x: x[1],reverse=True)
    t = [0 for _ in range(n)]
    d = [0 for _ in range(n)]
    for i in range(n):
        t[i] = td[i][0]
        d[i] = td[i][1]
    dsum = [0 for _ in range(n+1)]
    for i in range(n):
        dsum[i+1] = dsum[i] + d[i]
    tset = set()
    tset.add(t[0])
    tsum = [0 for _ in range(n+1)]
    for i in range(n):
        tsum[i+1] = tsum[i] + t[i]
        tset.add(t[i])
    tsum2 = [0 for _ in range(n+1)]
    for i in range(n):
        tsum2[i+1] = tsum2[i] + t[i]*t[i]
    ans = 0
    for i in range(1,k+1):
        ans = max(ans,dsum[i] + i*i)
    for i in range(k+1,n+1):
        if t[i-1] in tset:
            continue
        tset.add(t[i-1])
        ans = max(ans,dsum[i] + tsum[i] + i*i)
    for i in range(k+1,n+1):
        if t[i-1] not in tset:
            continue
        tset.remove(t[i-1])
        ans = max(ans,dsum[i] + tsum[i-1] + i*i - tsum2[i-1])
    print(ans)
