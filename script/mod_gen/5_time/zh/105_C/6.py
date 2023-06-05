def convert_to_base2(num):
    if num == 0:
        return "0"
    res = ""
    while num != 0:
        res = str(num % (-2)) + res
        num = num // (-2)
    return res

if __name__ == '__main__':
    convert_to_base2()