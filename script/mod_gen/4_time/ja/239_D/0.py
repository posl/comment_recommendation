def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(B+1, 100):
    if is_prime(i):
        B = i
        break
for i in range(C-1, 0, -1):
    if is_prime(i):
        C = i
        break

if __name__ == '__main__':
    is_prime()