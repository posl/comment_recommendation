def base_to_decimal(base, num):
    num = str(num)
    result = 0
    for i in range(len(num)):
        result += int(num[len(num) - 1 - i]) * pow(base, i)
    return result

if __name__ == '__main__':
    base_to_decimal()