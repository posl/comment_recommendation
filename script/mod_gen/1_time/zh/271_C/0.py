def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=1
    for i in range(n):
        ans*=a[i]-i
        ans%=10**9+7
    print(ans)
main()
