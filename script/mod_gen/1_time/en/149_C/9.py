def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True
X = int(input())
while not isPrime(X):
    X += 1
print(X)

if __name__ == '__main__':
    isPrime()