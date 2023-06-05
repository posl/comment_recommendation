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
mod = 10**9+7
n, m = map(int, input().split())
arr = factorization(m)
ans = 1
for i in range(len(arr)):
    ans *= arr[i][1] + n - 1
    ans %= mod
print(ans)
