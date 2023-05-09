def main():
    N = int(input())
    MOD = 10**9 + 7
    print((10**N - 2 * (9**N) + 8**N) % MOD)

if __name__ == '__main__':
    main()