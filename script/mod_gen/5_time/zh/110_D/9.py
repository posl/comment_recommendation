def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr
mod = 10**9+7
N,M = map(int,input().split())
ans = 1
for i in factorization(M):
    ans *= i[1]+N-1
    ans %= mod
print(ans)

if __name__ == '__main__':
    factorization()