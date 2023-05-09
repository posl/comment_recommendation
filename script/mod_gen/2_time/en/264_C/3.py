def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for h in range(H1 - H2 + 1):
        for w in range(W1 - W2 + 1):
            if A[h][w] == B[0][0]:
                for i in range(H2):
                    for j in range(W2):
                        if A[h + i][w + j] != B[i][j]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()