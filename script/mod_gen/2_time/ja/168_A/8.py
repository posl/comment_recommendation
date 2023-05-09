def main():
    N = int(input())
    N = N % 10
    if N in [2, 4, 5, 7, 9]:
        print('hon')
    elif N in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')

if __name__ == '__main__':
    main()