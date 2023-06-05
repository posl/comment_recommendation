def print_hex(n):
    if n < 10:
        print("0"+str(n))
    else:
        print(hex(n).upper()[2:])

if __name__ == '__main__':
    print_hex()