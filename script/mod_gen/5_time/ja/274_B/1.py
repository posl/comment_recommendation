def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(H):
        X = 0
        for j in range(W):
            if C[i][j] == "#":
                X += 1
        print(X, end=" ")
    print()

if __name__ == '__main__':
    main()