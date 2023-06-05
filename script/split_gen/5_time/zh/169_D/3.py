def factorization(n):
    #素因数分解
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
factors = factorization(n)
ans = 0
for factor in factors:
    cnt = 0
    temp = n
    while temp % factor[0] == 0:
        cnt += 1
        temp //= factor[0]
    n //= factor[0] ** cnt
    ans += cnt
print(ans)
