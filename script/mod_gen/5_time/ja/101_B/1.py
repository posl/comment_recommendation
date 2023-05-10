def getSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n / 10)
    return sum
N = int(input())

if __name__ == '__main__':
    getSumOfDigits()