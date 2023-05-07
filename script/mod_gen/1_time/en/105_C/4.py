def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    S = ''
    while N != 0:
        if N % 2 == 0:
            S += '0'
            N //= -2
        else:
            S += '1'
            N = (N - 1) // -2
    print(S[::-1])

if __name__ == '__main__':
    main()