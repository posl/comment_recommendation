def main():
    N = int(input())
    if N <= 21:
        print('AGC' + str(100 + N)[1:4])
    else:
        print('AGC' + str(100 + N + 1)[1:4])

if __name__ == '__main__':
    main()