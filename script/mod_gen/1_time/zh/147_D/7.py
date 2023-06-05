def solve(n, a):
    ans=0
    for i in range(60):
        one=0
        for j in range(n):
            if a[j]>>i & 1:
                one+=1
        ans+=one*(n-one)*(1<<i)
    return ans%((10**9)+7)
n=int(input())
a=list(map(int, input().split()))
print(solve(n, a))
