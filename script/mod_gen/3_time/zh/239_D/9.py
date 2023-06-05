def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    for j in range(c, d+1):
        if isPrime(i+j):
            print("青木")
            exit()
print("高桥")

if __name__ == '__main__':
    isPrime()