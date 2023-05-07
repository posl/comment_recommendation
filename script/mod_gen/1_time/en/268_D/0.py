def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            if len(S[i] + S[j]) > 16:
                break
            for k in range(j + 1, N):
                if len(S[i] + S[j] + S[k]) > 16:
                    break
                X = S[i] + '_' + S[j] + '_' + S[k]
                if X not in T:
                    print(X)
                    return
    print(-1)

if __name__ == '__main__':
    main()