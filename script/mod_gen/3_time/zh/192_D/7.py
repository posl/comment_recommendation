def to_decimal(x, radix):
    x = x[::-1]
    num = 0
    for i in range(len(x)):
        num += int(x[i]) * radix ** i
    return num

if __name__ == '__main__':
    to_decimal()