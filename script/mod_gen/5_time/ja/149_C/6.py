def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

if __name__ == '__main__':
    is_prime()