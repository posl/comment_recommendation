def main():
    N = int(input())
    S_N = sum([int(n) for n in str(N)])
    if N % S_N == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()