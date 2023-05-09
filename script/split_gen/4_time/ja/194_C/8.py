def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans+=a[i]*a[i]*(n-1)
        for j in range(i+1,n):
            ans-=2*a[i]*a[j]
    print(ans)
