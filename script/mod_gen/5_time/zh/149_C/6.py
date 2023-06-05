def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
X = int(input())
while not is_prime(X):
    X += 1
print(X)

if __name__ == '__main__':
    is_prime()