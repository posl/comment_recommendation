def calc(n,k):
    if k%2==0:
        tmp = n//k
        return tmp**3 + (n+k//2)//k**3
    else:
        tmp = n//k
        return tmp**3
n,k = map(int,input().split())
ans = calc(n,k)
print(ans)
