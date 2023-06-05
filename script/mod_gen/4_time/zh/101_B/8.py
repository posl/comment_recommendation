def sumDigits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum

if __name__ == '__main__':
    sumDigits()