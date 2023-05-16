def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))
x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1

if __name__ == '__main__':
    isPrime()