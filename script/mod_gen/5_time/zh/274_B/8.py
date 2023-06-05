def problem274_b():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(W):
        X = 0
        for j in range(H):
            if C[j][i] == "#":
                X += 1
        print(X, end=" ")
    print("")

if __name__ == '__main__':
    problem274_b()