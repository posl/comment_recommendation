def main():
    N = int(input())
    print((pow(10, N, 10**9+7) - 2*pow(9, N, 10**9+7) + pow(8, N, 10**9+7)) % (10**9+7))

if __name__ == '__main__':
    main()