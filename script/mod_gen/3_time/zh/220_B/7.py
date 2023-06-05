def toDecimal(num, base):
    num = str(num)
    result = 0
    for i in range(len(num)):
        result += int(num[-i - 1]) * (base ** i)
    return result

if __name__ == '__main__':
    toDecimal()