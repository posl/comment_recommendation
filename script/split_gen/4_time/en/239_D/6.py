def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if isPrime(i+j):
            print("Takahashi")
            exit()
print("Aoki")
