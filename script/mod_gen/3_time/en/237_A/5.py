def main():
    n = int(input())
    if n >= -2**31 and n < 2**31:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()