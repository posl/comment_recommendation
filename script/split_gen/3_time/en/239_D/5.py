def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return not any(n % i == 0 for i in range(3, int(n**0.5)+1, 2))
A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            print('Aoki')
            exit()
print('Takahashi')
