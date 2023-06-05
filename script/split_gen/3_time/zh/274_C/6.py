def distance(N,A):
    #初始化
    distance = [0]*(2*N+1)
    distance[1] = 0
    #计算
    for i in range(1,N+1):
        distance[2*i] = distance[i] + 1
        distance[2*i+1] = distance[i] + 1
    #返回
    return distance
