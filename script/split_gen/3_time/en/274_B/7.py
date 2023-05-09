def main():
    # H, W
    HW = list(map(int, input().split()))
    # C_{i, j}
    C = []
    for i in range(HW[0]):
        C.append(list(input()))
    # X_j
    X = [0] * HW[1]
    for j in range(HW[1]):
        for i in range(HW[0]):
            if C[i][j] == '#':
                X[j] += 1
    # Output
    print(' '.join(map(str, X)))
