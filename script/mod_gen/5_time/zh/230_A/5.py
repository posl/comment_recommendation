def main():
    N = int(input())
    if N <= 21:
        print('AGC0' + str(N))
    else:
        print('AGC' + str(N + 2))

if __name__ == '__main__':
    main()