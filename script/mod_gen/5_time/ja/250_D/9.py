def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not num & 1:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
n = int(input())
cnt = 0
for i in range(1, int(n ** 0.25) + 1):
    if n % i == 0:
        if is_prime(i):
            if n % (i ** 4) == 0:
                cnt += 1
        if is_prime(n // i):
            if n % ((n // i) ** 4) == 0:
                cnt += 1
print(cnt)

if __name__ == '__main__':
    is_prime()