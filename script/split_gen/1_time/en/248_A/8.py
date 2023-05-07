def main():
    # read the input
    S = input()
    # convert the string to a list of digits
    digits = list(map(int, list(S)))
    # the sum of the digits from 0 to 9
    # is 0+1+2+3+4+5+6+7+8+9 = 45
    sum_of_digits = sum(digits)
    # the sum of the digits from 0 to 9
    # is 0+1+2+3+4+5+6+7+8+9 = 45
    sum_of_all_digits = sum(range(10))
    # the missing digit is the difference between
    # the sum of all digits and the sum of the digits
    missing_digit = sum_of_all_digits - sum_of_digits
    # print the missing digit
    print(missing_digit)
