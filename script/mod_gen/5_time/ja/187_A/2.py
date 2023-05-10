def getSumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = int(num / 10)
    return sum
a, b = map(int, input().split())
print(getSumOfDigits(a) if getSumOfDigits(a) > getSumOfDigits(b) else getSumOfDigits(b))

if __name__ == '__main__':
    getSumOfDigits()