def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
Takahashi = 0
Aoki = 0
for i in range(A, B+1):
    if is_prime(i):
        Takahashi += 1
for i in range(C, D+1):
    if is_prime(i):
        Aoki += 1

if __name__ == '__main__':
    is_prime()