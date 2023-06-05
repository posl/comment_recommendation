def add_zero(num):
    num_str = str(num)
    while len(num_str) < 4:
        num_str = "0" + num_str
    return num_str
print(add_zero(int(input())))
