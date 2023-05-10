def prime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if prime(i + j):
            print('Takahashi')
            exit()
print('Aoki')
