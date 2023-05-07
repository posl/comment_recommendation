def main():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)
main()

if __name__ == '__main__':
    main()