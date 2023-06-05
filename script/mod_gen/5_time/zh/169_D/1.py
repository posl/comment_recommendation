def prime_factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct
N = int(input())
factors = prime_factorize(N)
ans = 0

if __name__ == '__main__':
    prime_factorize()