def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5)+1, 2):
        if x % i == 0:
            return False
    return True
x = int(input())
while not is_prime(x):
    x += 1
print(x)
