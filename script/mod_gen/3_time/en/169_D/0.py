def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
N = int(input())
prime_list = prime_factorize(N)
prime_list = list(set(prime_list))
ans = 0
for i in prime_list:
    tmp = N
    while tmp % i == 0:
        tmp //= i
    if tmp % i == 1:
        ans += 1
print(ans)

if __name__ == '__main__':
    prime_factorize()