def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True
X = int(input())
while not is_prime(X):
    X += 1
print(X)

if __name__ == '__main__':
    is_prime()