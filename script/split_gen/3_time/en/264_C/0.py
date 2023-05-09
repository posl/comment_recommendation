def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    # 2次元累積和
    S1 = [[0] * (W1 + 1) for _ in range(H1 + 1)]
    S2 = [[0] * (W2 + 1) for _ in range(H2 + 1)]
    for i in range(H1):
        for j in range(W1):
            S1[i + 1][j + 1] = S1[i][j + 1] + S1[i + 1][j] - S1[i][j] + A[i][j]
    for i in range(H2):
        for j in range(W2):
            S2[i + 1][j + 1] = S2[i][j + 1] + S2[i + 1][j] - S2[i][j] + B[i][j]
    # 2次元累積和の差分
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if S1[i + H2][j + W2] - S1[i + H2][j] - S1[i][j + W2] + S1[i][j] == S2[H2][W2]:
                print("Yes")
                return
    print("No")
