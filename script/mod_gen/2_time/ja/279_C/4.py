def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    for i in range(H):
        if S[i] == T[i]:
            continue
        else:
            for j in range(W):
                if S[i][j] == T[i][j]:
                    continue
                else:
                    for k in range(H):
                        if S[k][j] == T[i][j]:
                            S[i], S[k] = S[k], S[i]
                            break
                    else:
                        print('No')
                        return
    print('Yes')

if __name__ == '__main__':
    main()