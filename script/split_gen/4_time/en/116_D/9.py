def main():
    #input
    N,K = map(int,input().split())
    TD = [list(map(int,input().split())) for _ in range(N)]
    #solve
    TD.sort(key=lambda x:x[1],reverse=True)
    tset = set()
    tlist = []
    i = 0
    while len(tlist) < K:
        if TD[i][0] not in tset:
            tset.add(TD[i][0])
            tlist.append(TD[i][0])
        i += 1
    ans = sum([TD[j][1] for j in range(K)])
    ans += len(tlist)**2
    for j in range(K,N):
        if TD[j][0] not in tset:
            tset.add(TD[j][0])
            tlist.append(TD[j][0])
            ans += TD[j][1] - TD[i][1]
            ans += 2*len(tlist) - 1
            i += 1
    #output
    print(ans)
