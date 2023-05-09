def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
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