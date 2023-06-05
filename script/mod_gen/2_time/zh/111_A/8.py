def prime_factorize(n):
    a=[]
    while n%2==0:
        a.append(2)
        n//=2
    f=3
    while f*f<=n:
        if n%f==0:
            a.append(f)
            n//=f
        else:
            f+=2
    if n!=1:
        a.append(n)
    return a
n,m=map(int,input().split())
mod=10**9+7
f=prime_factorize(m)
f=list(set(f))
f.sort()
size=len(f)
cnt=[0]*size
for i in range(size):
    while m%f[i]==0:
        cnt[i]+=1
        m//=f[i]

if __name__ == '__main__':
    prime_factorize()