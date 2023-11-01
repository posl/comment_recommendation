def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1): #只需要判定到根号n
        if n % i == 0:
            re

if __name__ == '__main__':
    isPrime()