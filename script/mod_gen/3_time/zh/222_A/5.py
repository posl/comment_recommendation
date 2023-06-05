def add_zero(n):
    if n < 0 or n > 9999:
        print("输入的数字超出范围")
    else:
        if n < 10:
            print("000" + str(n))
        elif n < 100:
            print("00" + str(n))
        elif n < 1000:
            print("0" + str(n))
        else:
            print(n)
add_zero(1)
add_zero(11)
add_zero(111)
add_zero(1111)
add_zero(11111)
add_zero(111111)
add_zero(1111111)
