def is_multiple_of_9(number):
    sum_of_digits = 0
    for digit in number:
        sum_of_digits += int(digit)
    return sum_of_digits % 9 == 0
