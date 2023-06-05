def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        i = 3
        while i <= int(num ** 0.5) + 1:
            if num % i == 0:
                return False
            i += 2
        return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1
