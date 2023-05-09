def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(100):
    if is_prime(A + i):
        print("Takahashi")
        exit()
    elif is_prime(C + i):
        print("Aoki")
        exit()
