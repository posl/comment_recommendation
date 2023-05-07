def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(1, 1 << N):
        X = ''
        for j in range(N):
            if i & (1 << j):
                X += S[j]
            else:
                X += '_'
        if 3 <= len(X) <= 16 and X not in T:
            print(X)
            return
    print(-1)

if __name__ == '__main__':
    main()