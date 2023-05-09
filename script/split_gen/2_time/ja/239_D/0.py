def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(c, d+1):
    if is_prime(a + i):
        print('Takahashi')
        exit()
for i in range(a, b+1):
    if not is_prime(i + d):
        print('Aoki')
        exit()
print('Takahashi')
