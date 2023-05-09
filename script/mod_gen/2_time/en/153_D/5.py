def main():
    H = int(input())
    if H == 1:
        print(1)
    else:
        print(2**H.bit_length() - 1)

if __name__ == '__main__':
    main()