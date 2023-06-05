def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True
X = int(input())
while not is_prime(X):
    X += 1
print(X)

if __name__ == '__main__':
    is_prime()