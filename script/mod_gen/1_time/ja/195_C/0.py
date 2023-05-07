def main():
    N = int(input())
    if N < 1000:
        print(0)
    elif N < 1000000:
        print(N - 999)
    elif N < 1000000000:
        print((N - 999999) * 2 + 999)
    elif N < 1000000000000:
        print((N - 999999999) * 3 + 1998)
    elif N < 1000000000000000:
        print((N - 999999999999) * 4 + 2997)
    else:
        print((N - 999999999999999) * 5 + 3996)

if __name__ == '__main__':
    main()