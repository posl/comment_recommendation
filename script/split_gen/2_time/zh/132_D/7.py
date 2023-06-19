def f(n,k):
    if n<k:
        return 0
    if k==0:
        return 1
    return f(n-1,k-1)+f(n-1,k)
n,k=map(int,input().split())
print(f(n,k)%1000000007)
for i in range(2,k+1):
    print((f(n,i)-f(n,i-1))%1000000007)
