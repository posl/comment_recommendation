def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i += 2
    return True
x = int(input())
while not is_prime(x):
    x += 1
print(x)

if __name__ == '__main__':
    is_prime()