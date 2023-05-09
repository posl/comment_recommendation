def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    print(*sorted(S, key=lambda x: [X.index(c) for c in x]), sep='
')

if __name__ == '__main__':
    main()