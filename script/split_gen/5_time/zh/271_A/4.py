def main():
    n = int(input())
    if n < 16:
        print('0' + hex(n)[2:])
    else:
        print(hex(n)[2:])
