def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    for s in sorted(S, key=lambda s: [X.index(c) for c in s]):
        print(s)

if __name__ == '__main__':
    main()