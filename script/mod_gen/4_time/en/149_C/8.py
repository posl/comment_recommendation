def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    X += 1

if __name__ == '__main__':
    is_prime()