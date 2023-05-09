def main():
    H1, W1 = [int(x) for x in input().split()]
    A = [[int(x) for x in input().split()] for _ in range(H1)]
    H2, W2 = [int(x) for x in input().split()]
    B = [[int(x) for x in input().split()] for _ in range(H2)]
    for i in range(H1):
        for j in range(W1):
            if i < H2 and j < W2:
                if A[i][j] != B[i][j]:
                    print('No')
                    return
            elif i < H2 or j < W2:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()