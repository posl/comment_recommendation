def isPrime(n): #素数判定
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())

if __name__ == '__main__':
    isPrime()