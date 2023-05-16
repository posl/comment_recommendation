def main():
    # input
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    # compute
    for i1 in range(H):
        for i2 in range(i1+1, H):
            for j1 in range(W):
                for j2 in range(j1+1, W):
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        print('No')
                        exit()
    # output
    print('Yes')

if __name__ == '__main__':
    main()