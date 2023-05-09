def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    B = []
    for i in range(H):
        if '#' in A[i]:
            B.append(A[i])
    C = []
    for j in range(W):
        if '#' in [A[i][j] for i in range(H)]:
            C.append(j)
    for i in range(len(B)):
        print(''.join([B[i][j] for j in C]))
    return

if __name__ == '__main__':
    main()