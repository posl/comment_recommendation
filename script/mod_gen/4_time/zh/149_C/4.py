def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True
x = int(input())
while True:
    if isPrime(x):
        print(x)
        exit()
    x += 1

if __name__ == '__main__':
    isPrime()