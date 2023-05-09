def convertToHex(n):
    if n < 16:
        return "0" + hex(n)[2:].upper()
    else:
        return hex(n)[2:].upper()
