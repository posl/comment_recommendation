def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    print(solve(N, X, L))

if __name__ == '__main__':
    main()