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
a, b, c, d = map(int, input().split())
count = 0
for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i + j):
            count += 1

if __name__ == '__main__':
    is_prime()