def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(*S[::-1], sep='
')

if __name__ == '__main__':
    main()