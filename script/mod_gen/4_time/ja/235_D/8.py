def solve(a,n):
    #print(a,n)
    if a==1:
        return n-1
    ans=0
    while n>0:
        ans+=1
        if n%a==0:
            n//=a
        else:
            n-=1
    return ans
a,n=map(int,input().split())
print(solve(a,n))

if __name__ == '__main__':
    solve()