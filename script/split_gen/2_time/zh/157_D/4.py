def getFriends(N,M,K,AB,CD):
    #先建立邻接表
    adj = [[] for _ in range(N)]
    for i in range(M):
        adj[AB[i][0]-1].append(AB[i][1]-1)
        adj[AB[i][1]-1].append(AB[i][0]-1)
    #print(adj)
    #再建立阻隔表
    block = [[] for _ in range(N)]
    for i in range(K):
        block[CD[i][0]-1].append(CD[i][1]-1)
        block[CD[i][1]-1].append(CD[i][0]-1)
    #print(block)
    #最后判断是否是候选好友
    res = []
    for i in range(N):
        tmp = 0
        for j in range(N):
            if i!=j and j not in adj[i] and j not in block[i]:
                tmp += 1
        res.append(tmp)
    return res
