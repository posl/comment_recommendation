def convert_to_hexa(num):
    if num <= 15:
        return "0"+hex(num).replace("0x", "").upper()
    else:
        return hex(num).replace("0x", "").upper()
