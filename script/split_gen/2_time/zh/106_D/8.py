def main():
    #读取输入
    N,M,Q = map(int,input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i],R[i] = map(int,input().split())
    P = [0]*Q
    Q = [0]*Q
    for i in range(Q):
        P[i],Q[i] = map(int,input().split())
    #处理输入
    #预处理
    pre = [0]*N
    for i in range(M):
        pre[L[i]-1] += 1
        if R[i] != N:
            pre[R[i]] -= 1
    for i in range(1,N):
        pre[i] += pre[i-1]
    #处理查询
    for i in range(Q):
        print(pre[Q[i]-1]-pre[P[i]-1])
    return 0
