def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
x = int(input())
while not is_prime(x):
    x += 1
print(x)
