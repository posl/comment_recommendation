def main():
    mod = 10 ** 9 + 7
    N = int(input())
    print((10 ** N - 2 * 9 ** N + 8 ** N) % mod)

if __name__ == '__main__':
    main()