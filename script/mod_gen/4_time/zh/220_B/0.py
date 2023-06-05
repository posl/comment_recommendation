def convert_to_decimal(num, base):
    multiplier, result = 1, 0
    while num > 0:
        result += num % 10 * multiplier
        multiplier *= base
        num = num // 10
    return result

if __name__ == '__main__':
    convert_to_decimal()