def get_int(num_str, base):
    num = 0
    for i in range(len(num_str)):
        num += int(num_str[i]) * (base ** (len(num_str) - i - 1))
    return num
