def main():
    # H, W = map(int, input().split())
    # for i in range(H):
    #     A = list(map(int, input().split()))
    #     print(A)
    #     for j in range(W):
    #         B = A[j][i]
    #         print(B)
    #         print(' '.join(map(str, B)))
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    for i in range(W):
        for j in range(H):
            B = A[j][i]
            print(B)
        print(' '.join(map(str, B)))

if __name__ == '__main__':
    main()