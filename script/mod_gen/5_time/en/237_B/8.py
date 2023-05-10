def main():
    H,W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    for i in range(W):
        print(" ".join(map(str, B[i])))

if __name__ == '__main__':
    main()