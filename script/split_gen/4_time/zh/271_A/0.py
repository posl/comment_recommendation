def print_hex(n):
    if n < 10:
        print("0"+str(n))
    else:
        print(hex(n).upper()[2:])
