def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    # print(A)
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    # print(B)
    for i in range(W):
        print(*B[i])
    return 0

if __name__ == '__main__':
    main()