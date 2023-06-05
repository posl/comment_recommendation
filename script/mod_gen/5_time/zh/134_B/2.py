def main():
    N,D = input().split()
    N = int(N)
    D = int(D)
    if N % (2 * D + 1) == 0:
        print(N // (2 * D + 1))
    else:
        print(N // (2 * D + 1) + 1)

if __name__ == '__main__':
    main()