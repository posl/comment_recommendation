def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number //= 10
    return result

if __name__ == '__main__':
    convert_to_decimal()