def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    if N == 1:
        for i in range(3, 17):
            for j in range(1, i):
                X = S[0] + '_' * j
                if X not in T:
                    print(X)
                    return
        print(-1)
        return
    for i in range(3, 17):
        for j in range(1, i):
            for k in range(1, i):
                X = S[0] + '_' * j + S[1] + '_' * k
                if X not in T:
                    print(X)
                    return
    print(-1)

if __name__ == '__main__':
    main()