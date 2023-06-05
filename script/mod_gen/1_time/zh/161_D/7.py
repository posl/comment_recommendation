def isLuckyNum(number):
    if number < 10:
        return True
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    digits.reverse()
    for i in range(1, len(digits)):
        if abs(digits[i] - digits[i-1]) > 1:
            return False
    return True

if __name__ == '__main__':
    isLuckyNum()