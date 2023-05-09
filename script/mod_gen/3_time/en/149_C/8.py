def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
X = int(input())
while True:
    if isPrime(X):
        print(X)
        break
    X += 1
import math

if __name__ == '__main__':
    isPrime()