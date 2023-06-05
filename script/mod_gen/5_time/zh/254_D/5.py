def getSquareNumber(num):
    i = 1
    while i * i <= num:
        if i * i == num:
            return i
        i += 1
    return -1
N = int(input())
result = 0
for i in range(1, N + 1):
    squareNumber = getSquareNumber(i)
    if squareNumber != -1:
        result += 2
print(result)

if __name__ == '__main__':
    getSquareNumber()