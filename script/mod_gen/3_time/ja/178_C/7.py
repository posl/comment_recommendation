def main():
    N = int(input())
    MOD = 10**9+7
    print((9**N + 7**N - 8**N)%MOD)

if __name__ == '__main__':
    main()