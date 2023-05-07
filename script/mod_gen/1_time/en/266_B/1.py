def main():
    N = int(input())
    print((N - N // 998244353 * 998244353) % 998244353)

if __name__ == '__main__':
    main()