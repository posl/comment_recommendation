def main():
    n,c=map(int,input().strip().split())
    d=[list(map(int,input().strip().split())) for _ in range(c)]
    c=[list(map(int,input().strip().split())) for _ in range(n)]
    m=[0]*c
    for i in range(n):
        for j in range(n):
            m[(i+j)%3]+=d[c[i][j]-1]
    ans=10**9
    for i in range(c):
        for j in range(c):
            if i==j:continue
            for k in range(c):
                if i==k or j==k:continue
                ans=min(ans,m[i]+m[j]+m[k])
    print(ans)

if __name__ == '__main__':
    main()