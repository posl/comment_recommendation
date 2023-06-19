def cal():
    N,M = map(int,input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int,input().split())))
    ans = 0
    for sign in range(8):
        cakes.sort(key=lambda x: (sign&1)*x[0]-(sign&2)*x[0]-(sign&4)*x[0],reverse=True)
        sum = [0,0,0]
        for i in range(M):
            for j in range(3):
                sum[j] += cakes[i][j]
        ans = max(ans,abs(sum[0])+abs(sum[1])+abs(sum[2]))
    print(ans)
