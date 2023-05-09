def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    i = 3
    while i <= x ** 0.5:
        if x % i == 0:
            return False
        i += 2
    return True
a, b, c, d = map(int, input().split())
for i in range(b, d+1):
    if is_prime(i) == True:
        print("Aoki")
        exit()
print("Takahashi")
