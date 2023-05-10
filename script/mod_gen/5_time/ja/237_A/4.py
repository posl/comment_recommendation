def main():
    N = int(input())
    if -2**31 <= N and N < 2**31:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()