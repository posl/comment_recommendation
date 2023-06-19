def main():
    n,a,b = map(int,input().split())
    if a+b>n:
        print(0)
    else:
        ans = pow(2,n,10**9+7)-1
        for i in range(n-a+1,n-b+1):
            ans -= comb(n,i,10**9+7)
        print(ans%(10**9+7))
