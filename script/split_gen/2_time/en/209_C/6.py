def main():
    N=int(input())
    C=list(map(int,input().split()))
    MOD=10**9+7
    ans=1
    for i in range(N):
        if i==0:
            ans*=C[i]
        else:
            ans*=max(0,C[i]-i)
            ans%=MOD
    print(ans)
