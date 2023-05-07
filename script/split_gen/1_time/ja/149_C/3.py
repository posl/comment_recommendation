def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
        return True
X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    else:
        X += 1
