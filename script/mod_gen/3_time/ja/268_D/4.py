def main():
    import itertools
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    for i in range(3, 17):
        L = list(itertools.product(S, repeat=i))
        for j in range(len(L)):
            X = ''.join(L[j])
            for k in range(M):
                if X == T[k]:
                    break
                elif k == M-1:
                    print(X)
                    return
    print(-1)

if __name__ == '__main__':
    main()