def main():
    n = input()
    if int(n) >= -2**31 and int(n) <= 2**31-1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()