def main():
    line = input()
    H, W = line.split()
    H = int(H)
    W = int(W)
    C = []
    for i in range(H):
        line = input()
        C.append(line)
    for j in range(W):
        X_j = 0
        for i in range(H):
            if C[i][j] == "#":
                X_j += 1
        print(X_j, end=" ")
    print()
main()
