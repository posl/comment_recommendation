def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

if __name__ == '__main__':
    main()