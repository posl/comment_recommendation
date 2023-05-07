def isPrime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+2, 2):
            if n % i == 0:
                return False
        return True
A, B, C, D = map(int, input().split())
for i in range(B, D+1):
    if isPrime(i):
        print('Aoki')
        exit()
print('Takahashi')
exit()

if __name__ == '__main__':
    isPrime()