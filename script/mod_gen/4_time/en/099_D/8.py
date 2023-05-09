def main():
    N,C = map(int,input().split())
    D = [list(map(int,input().split())) for i in range(C)]
    c = [list(map(int,input().split())) for i in range(N)]
    mod = [0]*3
    for i in range(N):
        for j in range(N):
            mod[(i+j)%3] += D[c[i][j]-1][:]
    ans = 10**9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i==j or j==k or k==i:
                    continue
                ans = min(ans,mod[0][i]+mod[1][j]+mod[2][k])
    print(ans)

if __name__ == '__main__':
    main()