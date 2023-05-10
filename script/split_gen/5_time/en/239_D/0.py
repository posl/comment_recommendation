def isPrime(n):
    if n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if isPrime(i+j):
            print("Aoki")
            exit()
print("Takahashi")
