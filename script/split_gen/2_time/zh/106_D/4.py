def main():
    #读取输入
    N,M,Q = map(int,input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i],R[i] = map(int,input().split())
    p = [0]*Q
    q = [0]*Q
    for i in range(Q):
        p[i],q[i] = map(int,input().split())
    #计算答案
    #每个城市的列车数量
    trains = [0]*(N+1)
    for i in range(M):
        for j in range(L[i],R[i]+1):
            trains[j]+=1
    #每个城市的列车数量的前缀和
    trains_prefix = [0]*(N+1)
    trains_prefix[1] = trains[1]
    for i in range(2,N+1):
        trains_prefix[i] = trains_prefix[i-1]+trains[i]
    #每个查询的答案
    for i in range(Q):
        print(trains_prefix[q[i]]-trains_prefix[p[i]-1])
