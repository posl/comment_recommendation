def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    print(*sorted(S, key=lambda s: [X.index(c) for c in s]), sep='
')

if __name__ == '__main__':
    main()