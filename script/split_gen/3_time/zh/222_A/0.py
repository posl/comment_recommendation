def print_4_digit_number(number):
    if number < 10:
        print("000" + str(number))
    elif number < 100:
        print("00" + str(number))
    elif number < 1000:
        print("0" + str(number))
    else:
        print(str(number))
