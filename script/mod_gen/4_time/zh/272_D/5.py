def main():
    N,M=map(int,input().split())
    result=[[-1 for i in range(N)] for j in range(N)]
    result[0][0]=0
    for i in range(N):
        for j in range(N):
            if result[i][j]!=-1:
                if i-1>=0 and result[i-1][j]==-1:
                    result[i-1][j]=result[i][j]+1
                if i+1<N and result[i+1][j]==-1:
                    result[i+1][j]=result[i][j]+1
                if j-1>=0 and result[i][j-1]==-1:
                    result[i][j-1]=result[i][j]+1
                if j+1<N and result[i][j+1]==-1:
                    result[i][j+1]=result[i][j]+1
    for i in range(N):
        print(" ".join(map(str,result[i])))

if __name__ == '__main__':
    main()