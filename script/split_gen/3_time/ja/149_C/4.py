def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    return pow(2, x-1, x) == 1
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1
