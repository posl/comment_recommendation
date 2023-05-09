def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    i = 3
    while i <= x**0.5:
        if x % i == 0:
            return False
        i += 2
    return True
x = int(input())
while not is_prime(x):
    x += 1
print(x)
