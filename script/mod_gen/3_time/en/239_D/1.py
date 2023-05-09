def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(A, B + 1):
    for j in range(C, D + 1):
        if is_prime(i + j):
            print('Aoki')
            exit()
print('Takahashi')

if __name__ == '__main__':
    is_prime()