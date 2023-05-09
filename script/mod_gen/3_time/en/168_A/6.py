def main():
    n = int(input())
    if n == 3:
        print('bon')
    elif n % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('hon')

if __name__ == '__main__':
    main()