def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
x = int(input())
while not isPrime(x):
    x += 1
print(x)

if __name__ == '__main__':
    isPrime()