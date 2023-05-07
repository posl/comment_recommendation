def main():
    N,K=map(int,input().split())
    T=[list(map(int,input().split())) for _ in range(N)]
    ans=0
    for i in range(N):
        for j in range(N):
            if T[i][j]==0:
                T[i][j]=10**9+1
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for

if __name__ == '__main__':
    main()