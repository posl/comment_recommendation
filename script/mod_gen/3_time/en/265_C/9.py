def main():
    H,W=map(int,input().split())
    G=[input() for _ in range(H)]
    d=[(0,1),(1,0),(0,-1),(-1,0)]
    v=[[-1]*W for _ in range(H)]
    v[0][0]=0
    i,j=0,0
    while True:
        if G[i][j]=='U':
            i-=1
        elif G[i][j]=='D':
            i+=1
        elif G[i][j]=='L':
            j-=1
        elif G[i][j]=='R':
            j+=1
        if i<0 or i>=H or j<0 or j>=W:
            break
        if v[i][j]>=0:
            print(-1)
            exit()
        v[i][j]=0
    print(i+1,j+1)

if __name__ == '__main__':
    main()