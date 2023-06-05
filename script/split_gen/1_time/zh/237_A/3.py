def is_int_32(num):
    if num >= -2**31 and num <= 2**31-1:
        print("是")
    else:
        print("否")
