def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    i = 3
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += 2
    return True
x = int(input())
while not is_prime(x):
    x += 1
print(x)
