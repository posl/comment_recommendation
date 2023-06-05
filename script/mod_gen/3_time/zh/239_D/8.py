def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
a, b, c, d = map(int, input().split())
g = 0
for i in range(a, b + 1):
    if is_prime(i):
        g = i
        break
for i in range(c, d + 1):
    if is_prime(i):
        if i - g > 0:
            print("青木")
        else:
            print("高桥")
        break

if __name__ == '__main__':
    is_prime()