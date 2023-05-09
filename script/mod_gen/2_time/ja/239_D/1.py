def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
A, B, C, D = map(int, input().split())
takahashi = 0
aoki = 0
for i in range(A, B + 1):
    for j in range(C, D + 1):
        if is_prime(i + j):
            aoki += 1
        else:
            takahashi += 1

if __name__ == '__main__':
    is_prime()