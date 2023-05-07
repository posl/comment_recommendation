def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    # 90度回転
    S90 = ["".join([S[j][i] for j in range(N-1, -1, -1)]) for i in range(N)]
    # 180度回転
    S180 = ["".join([S[i][j] for j in range(N-1, -1, -1)]) for i in range(N-1, -1, -1)]
    # 270度回転
    S270 = ["".join([S[j][i] for j in range(N)]) for i in range(N-1, -1, -1)]
    # 横反転
    Srev = ["".join([S[i][j] for j in range(N-1, -1, -1)]) for i in range(N)]
    # 90度回転 + 横反転
    S90rev = ["".join([Srev[j][i] for j in range(N-1, -1, -1)]) for i in range(N)]
    # 180度回転 + 横反転
    S180rev = ["".join([Srev[i][j] for j in range(N-1, -1, -1)]) for i in range(N-1, -1, -1)]
    # 270度回転 + 横反転
    S270rev = ["".join([Srev[j][i] for j in range(N)]) for i in range(N-1, -1, -1)]
    if S in [T, S90, S180, S270, Srev, S90rev, S180rev, S270rev]:
        print("Yes")
    else:
        print("No")
