def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for t in T:
        print(S.count(t))

if __name__ == '__main__':
    main()