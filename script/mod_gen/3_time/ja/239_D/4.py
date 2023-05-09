def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if isPrime(i+j):
            print("Aoki")
            exit()
print("Takahashi")

if __name__ == '__main__':
    isPrime()