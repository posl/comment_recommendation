def calc(n,k):
    if k == 1:
        return n+1
    elif k == n+1:
        return 1
    else:
        return n+1
n,k=map(int,input().split())
ans = 0
for i in range(1,k+1):
    ans += calc(n,i)
    ans %= 10**9+7
print(ans)
