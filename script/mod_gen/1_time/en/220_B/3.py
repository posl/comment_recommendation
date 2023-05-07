def toDecimal(base, number):
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[i]) * (base ** (len(number) - i - 1))
    return decimal

if __name__ == '__main__':
    toDecimal()