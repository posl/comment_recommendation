def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        S = ''
        while N != 0:
            if N % 2 == 0:
                S = '0' + S
                N //= -2
            else:
                S = '1' + S
                N = (N - 1) // -2
        print(S)

if __name__ == '__main__':
    main()