def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    print(*S, sep='
')

if __name__ == '__main__':
    main()