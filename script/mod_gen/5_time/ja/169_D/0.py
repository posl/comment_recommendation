def prime_factorize(n):
    # 素因数分解
    # 素因数を格納するリスト
    f = []
    # 2から√n以下の整数で割っていく
    while n % 2 == 0:
        f.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        if n % i == 0:
            f.append(i)
            n //= i
        else:
            i += 2
    if n != 1:
        f.append(n)
    return f
n = int(input())
f = prime_factorize(n)
f.sort()
f = list(set(f))
ans = 0
for i in range(len(f)):
    if n % f[i] == 0:
        ans += 1
        n //= f[i]
print(ans)

if __name__ == '__main__':
    prime_factorize()