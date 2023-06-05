def toBaseNeg2(number):
    if number == 0:
        return '0'
    result = ''
    while number != 0:
        remainder = number % -2
        number = number // -2
        if remainder < 0:
            remainder += 2
            number += 1
        result = str(remainder) + result
    return result

if __name__ == '__main__':
    toBaseNeg2()