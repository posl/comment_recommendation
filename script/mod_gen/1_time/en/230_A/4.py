def main():
    N = int(input())
    if N <= 9:
        print('AGC00{}'.format(N))
    elif N <= 99:
        print('AGC0{}'.format(N))
    else:
        print('AGC{}'.format(N))

if __name__ == '__main__':
    main()