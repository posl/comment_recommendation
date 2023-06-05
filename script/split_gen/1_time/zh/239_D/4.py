def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if isPrime(i):
        for j in range(c, d+1):
            if isPrime(j):
                if i+j == 9:
                    print("高桥")
                    exit()
                else:
                    print("青木")
                    exit()
