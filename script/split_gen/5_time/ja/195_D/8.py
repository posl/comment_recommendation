def main():
    N, M, Q = map(int, input().split())
    WV = [[0 for i in range(2)] for j in range(N)]
    for i in range(N):
        WV[i] = list(map(int, input().split()))
    X = list(map(int, input().split()))
    Query = [[0 for i in range(2)] for j in range(Q)]
    for i in range(Q):
        Query[i] = list(map(int, input().split()))
    #print(N, M, Q)
    #print(WV)
    #print(X)
    #print(Query)
    for i in range(Q):
        #print(Query[i][0])
        #print(Query[i][1])
        #print(X[Query[i][0]-1:Query[i][1]])
        #print(sorted(X[Query[i][0]-1:Query[i][1]]))
        X2 = sorted(X[Query[i][0]-1:Query[i][1]])
        #print(X2)
        #print(len(X2))
        #print(WV)
        #print(len(WV))
        #print(WV[0][0])
        #print(len(WV[0]))
        #print(WV[0][1])
        #print(len(WV[0][1]))
        #print(WV[0][1][0])
        #print(len(WV[0][1][0]))
        #print(WV[0][1][1])
        #print(len(WV[0][1][1]))
        #print(WV[1][0])
        #print(len(WV[1]))
        #print(WV[1][1][0])
        #print(len(WV[1][1][0]))
        #print(WV[1][1][1])
        #print(len(WV[1][1][1]))
        #print(WV[2][0])
        #print(len(WV[2]))
        #print(WV[2][1][0])
        #print(len(WV[2][1][0]))
        #print(WV[2][1][1])
        #print(len(WV[2][1][1]))
        #print(WV[3][0])
        #print(len(WV[3]))
        #print(WV[3][1][0])
        #print(len(WV[3][
