def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort(key=lambda s: [X.index(x) for x in s])
    for s in S:
        print(s)

if __name__ == '__main__':
    main()