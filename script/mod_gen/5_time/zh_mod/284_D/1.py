def isPrime(n):
    if n <= 3:
        return n > 1
    if n % 6 != 1 and n % 6 != 5:
        return False
    for i in range(5, int(n**0.5)+1,

if __name__ == '__main__':
    isPrime()