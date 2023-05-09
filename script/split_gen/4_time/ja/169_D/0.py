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
n = int(input())
f = factorization(n)
ans = 0
for x in f:
    e = x[1]
    i = 1
    while e >= i:
        ans += 1
        e -= i
        i += 1
print(ans)
