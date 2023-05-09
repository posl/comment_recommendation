def convert_to_decimal(number, base):
    number = str(number)
    number = number[::-1]
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[i]) * (base ** i)
    return decimal
