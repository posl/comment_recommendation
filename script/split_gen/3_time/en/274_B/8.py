def main():
    # read H and W
    H, W = map(int, input().split())
    # read C
    C = []
    for i in range(H):
        C.append(input())
    # count boxes in each column
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    # print X
    for x in X:
        print(x, end=' ')
    print()
