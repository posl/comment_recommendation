def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
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

if __name__ == '__main__':
    is_prime()