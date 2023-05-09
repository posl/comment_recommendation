def sum_digits(num):
    # Converts integer to string, then loops through each character in the string
    # and adds it to a sum.
    num = str(num)
    sum = 0
    for c in num:
        sum += int(c)
    return sum
