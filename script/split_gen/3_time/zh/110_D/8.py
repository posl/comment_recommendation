def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
n,m=map(int,input().split())
mod=10**9+7
ans=1
for i in range(2,int(m**0.5)+1):
    if m%i==0:
        cnt=0
        while m%i==0:
            cnt+=1
            m//=i
        ans=ans*(cnt+n-1)%mod
