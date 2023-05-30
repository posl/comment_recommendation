def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr
N, M = map(int, input().split())
MOD = 10**9 + 7
ans = 1
for i in range(2, int(M**0.5)+1):
    if M % i == 0:
        ans *= pow(i, factorization(M).count([i, 1]))
        ans %= MOD
        M //= i**factorization(M).count([i, 1])
