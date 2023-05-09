def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
a, b, c, d = list(map(int, input().split()))
for i in range(100):
    if a + i <= b and c + i <= d:
        if is_prime(a + i + c + i):
            print("Aoki")
            break
    else:
        print("Takahashi")
        break
