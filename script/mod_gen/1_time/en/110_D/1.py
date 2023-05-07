def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
n,m=map(int,input().split())
mod=10**9+7
ans=1
for i,j in factorization(m):
    ans*=j+n-1
    ans%=mod
    ans*=pow(j,mod-2,mod)
    ans%=mod
print(ans)

if __name__ == '__main__':
    factorization()