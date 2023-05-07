def is_prime(x):
    if x == 1:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1
