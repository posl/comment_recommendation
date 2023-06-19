def problem271_a(n):
    if n < 10:
        print('0' + str(hex(n))[2:])
    else:
        print(str(hex(n))[2:])
