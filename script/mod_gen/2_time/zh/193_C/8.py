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
A = set()
for i in range(2, int(N**0.5)+1):
    if i**2 > N:
        break
    x = i**2
    while x <= N:
        A.add(x)
        x *= i
print(N - len(A))

if __name__ == '__main__':
    prime_factorize()