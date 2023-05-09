def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
A, B, C, D = map(int, input().split())
for i in range(B + 1, D + 1):
    if is_prime(i):
        print("Aoki")
        exit()
print("Takahashi")
