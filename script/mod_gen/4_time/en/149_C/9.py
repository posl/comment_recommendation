def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1

if __name__ == '__main__':
    isPrime()