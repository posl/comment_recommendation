def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if not n & 1: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                if i + j == 5:
                    print("Aoki")
                    exit()
print("Takahashi")
