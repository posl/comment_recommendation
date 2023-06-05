def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
N = int(input())
ans = 0
for i in range(2, int(N ** (1/4)) + 1):
    if isPrime(i):
        for j in range(2, int(N ** (1/3)) + 1):
            if i ** 3 * j > N:
                break
            if isPrime(j):
                ans += 1
print(ans)

if __name__ == '__main__':
    isPrime()