def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-1,-1,-1):
        if a[i]>ans:
            ans=a[i]
        else:
            if (ans-a[i])%2==1:
                ans=a[i]-1
    print(ans)
main()
