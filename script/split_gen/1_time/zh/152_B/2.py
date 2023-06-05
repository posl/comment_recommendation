def problem152_b(a,b):
    a = int(a)
    b = int(b)
    a_str = str(a)
    b_str = str(b)
    a_str = a_str * b
    b_str = b_str * a
    if a_str < b_str:
        print(a_str)
    else:
        print(b_str)
