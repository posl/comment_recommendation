def main():
    N = int(input())
    if N < 1000:
        print(0)
    else:
        N = N - 999
        N = N // 1000
        print(N * (N + 1) // 2 + N)

if __name__ == '__main__':
    main()