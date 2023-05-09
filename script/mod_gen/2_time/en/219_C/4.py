def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S = sorted(S, key=lambda x: [X.index(i) for i in x])
    for s in S:
        print(s)

if __name__ == '__main__':
    main()