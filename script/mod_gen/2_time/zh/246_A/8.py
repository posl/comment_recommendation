def solve(n,m,a,c):
    b=[0]*(m+1)
    for i in range(m+1):
        b[i]=c[i]
    for i in range(n+1):
        for j in range(m+1):
            b[j]-=a[i]
        for j in range(m,0,-1):
            b[j-1]+=b[j]
    return b

if __name__ == '__main__':
    solve()