def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    X = ""
    for i in range(N):
        for j in range(N):
            if i != j:
                X = S[i] + "_" + S[j]
                if X in T:
                    continue
                else:
                    print(X)
                    return
    print(-1)

if __name__ == '__main__':
    main()