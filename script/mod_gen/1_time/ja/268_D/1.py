def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for j in range(N):
            for k in range(j+1, N):
                D = [S[j], "_"*(i-len(S[j])-len(S[k])), S[k]]
                X = "".join(D)
                if len(X) == i and X not in T:
                    print(X)
                    return
    print(-1)

if __name__ == '__main__':
    main()