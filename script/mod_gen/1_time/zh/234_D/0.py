def solve(n,k,p):
    ans=[]
    for i in range(k,n+1):
        ans.append(max(p[i-k:i]))
    print(*ans,sep='\n')

if __name__ == '__main__':
    solve()