def main():
    N = input()
    N = N[::-1]
    N = N.lstrip('0')
    if N == N[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()