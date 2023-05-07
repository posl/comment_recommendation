def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1
