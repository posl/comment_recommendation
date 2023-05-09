def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
N = int(input())
count = 0
for i in range(2, int(N**0.5)+1):
    if isPrime(i):
        for j in range(3, 100):
            if i * (j**3) <= N:
                count += 1
            else:
                break
print(count)

if __name__ == '__main__':
    isPrime()