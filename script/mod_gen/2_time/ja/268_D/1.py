def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    for i in range(N):
        for j in range(M):
            if S[i] in T[j]:
                print(-1)
                return
    for i in range(2**N):
        x = ''
        for j in range(N):
            if (i >> j) & 1:
                x += S[j] + '_'
            else:
                x += '_' + S[j]
        if 3 <= len(x) <= 16:
            for j in range(M):
                if x == T[j]:
                    break
            else:
                print(x)
                return
    print(-1)

if __name__ == '__main__':
    main()