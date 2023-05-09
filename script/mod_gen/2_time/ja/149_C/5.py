def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
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

if __name__ == '__main__':
    is_prime()