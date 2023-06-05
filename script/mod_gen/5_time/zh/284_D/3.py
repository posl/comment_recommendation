def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True
t = int(input())
for i in range(t):
    n = int(input())
    p = 0
    q = 0
    for j in range(2, n):
        if isPrime(j) and n % j == 0:
            p = j
            q = int(n / p)
            break
    print(p, q)

if __name__ == '__main__':
    isPrime()