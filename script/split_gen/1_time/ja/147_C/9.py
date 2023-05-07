def main():
    N = int(input())
    #print(N)
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        #print(A[i])
        x = []
        y = []
        for j in range(A[i]):
            xj,yj = map(int,input().split())
            x.append(xj)
            y.append(yj)
        X.append(x)
        Y.append(y)
    #print(A)
    #print(X)
    #print(Y)
    ans = 0
    for i in range(2**N):
        bit = [0]*N
        for j in range(N):
            if (i>>j) & 1:
                bit[N-1-j] = 1
        #print(bit)
        flag = True
        for j in range(N):
            if bit[j] == 1:
                for k in range(A[j]):
                    if bit[X[j][k]-1] != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(bit))
    print(ans)
