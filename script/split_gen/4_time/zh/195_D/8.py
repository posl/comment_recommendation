def main():
    N,M,Q = map(int,input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = list(map(int,input().split()))
    Query = [0] * Q
    for i in range(Q):
        Query[i] = list(map(int,input().split()))
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X_temp = X[0:L-1] + X[R:]
        X_temp.sort()
        V_temp = V[0:L-1] + V[R:]
        V_temp.sort()
        W_temp = W[0:L-1] + W[R:]
        W_temp.sort()
        print(X_temp)
        print(V_temp)
        print(W_temp)
        print('**********')
        Sum = 0
        j = 0
        while j < len(X_temp):
            Sum += V_temp[j]
            j += 1
        print(Sum)
