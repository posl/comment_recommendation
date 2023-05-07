def convert_to_decimal(base, number):
    # Convert a number in base to decimal
    # base: integer
    # number: string
    # return: integer
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[-i-1]) * base**i
    return decimal
