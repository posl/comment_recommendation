def convertToBaseTwo(num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result

if __name__ == '__main__':
    convertToBaseTwo()