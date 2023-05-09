def findMinDivisor(num):
    if num % 2 == 0:
        return num
    else:
        return num * 2

if __name__ == '__main__':
    findMinDivisor()