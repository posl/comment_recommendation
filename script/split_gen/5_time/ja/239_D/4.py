def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if not n % k:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(100):
    if a <= c + i <= b and is_prime(c + i):
        print('Aoki')
        exit()
    if c <= a + i <= d and is_prime(a + i):
        print('Takahashi')
        exit()
