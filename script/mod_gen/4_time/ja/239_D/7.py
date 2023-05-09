def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if (n % 2) == 0:
        return False
    i = 3
    while i <= (n**0.5):
        if (n % i) == 0:
            return False
        i += 2
    return True
a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    if isPrime(i):
        for j in range(c,d+1):
            if isPrime(j):
                if i+j == 0:
                    print("Aoki")
                    exit()
print("Takahashi")

if __name__ == '__main__':
    isPrime()