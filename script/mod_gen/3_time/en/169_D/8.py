def prime_factorize(n):
    """nの素因数分解を返す"""
    divisors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            divisors.append(i)
            n //= i
    if n > 1:
        divisors.append(n)
    return divisors
N = int(input())
divisors = prime_factorize(N)
divisors.sort()

if __name__ == '__main__':
    prime_factorize()