def convert_to_decimal(num_str, radix):
    num = 0
    for i in range(len(num_str)):
        num += int(num_str[-i-1]) * radix ** i
    return num

if __name__ == '__main__':
    convert_to_decimal()