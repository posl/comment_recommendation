def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    # B の各要素が A のどこにあるかを確認する
    for i in range(H2):
        for j in range(W2):
            if B[i][j] not in A[i]:
                print('No')
                return
    # B の各要素が A のどこにあるかを確認する
    for i in range(H2):
        for j in range(W2):
            if B[i][j] not in A[i]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()