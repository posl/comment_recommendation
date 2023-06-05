def f(x):
    if x==0:
        return 0
    else:
        return 1+f(x//10)
N=int(input())
mod=998244353
ans=0
for i in range(1,10):
    if i<=N:
        ans+=i
    else:
        break
for i in range(1,18):
    if 10**i<=N:
        ans+=i*(min(N,10**(i+1)-1)-10**i+1)
    else:
        break
for i in range(1,18):
    if 10**i<=N:
        ans+=(10**i-1)//9
    else:
        break
print(ans%mod)
