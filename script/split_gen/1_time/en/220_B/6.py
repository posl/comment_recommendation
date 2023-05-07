def convertToDecimal(num, base):
    num = str(num)
    dec = 0
    for i, val in enumerate(num[::-1]):
        dec += int(val) * base ** i
    return dec
