def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): #nの平方根まで
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(100):
    if is_prime(A + i) and is_prime(C + i):
        print("Aoki")
        exit()
    elif is_prime(A + i):
        print("Takahashi")
        exit()
    elif is_prime(C + i):
        print("Aoki")
        exit()
    else:
        continue
