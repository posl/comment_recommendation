def problem272_b():
    N,M = map(int,input().split())
    x = [[0 for i in range(N)] for j in range(M)]
    for i in range(M):
        x[i] = list(map(int,input().split()))
    for i in range(M):
        for j in range(M):
            if i != j:
                if len(set(x[i][1:]) & set(x[j][1:])) > 0:
                    continue
                else:
                    print('No')
                    return
    print('Yes')
    return
problem272_b()
