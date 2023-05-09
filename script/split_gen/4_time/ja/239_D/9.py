def primecheck(n):
    if n == 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    else:
        return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if primecheck(i):
        for j in range(c, d+1):
            if primecheck(j):
                if primecheck(i+j):
                    print("Aoki")
                    exit()
print("Takahashi")
