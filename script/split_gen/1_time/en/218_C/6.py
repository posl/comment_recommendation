def main():
    N = int(input())
    S = [input() for i in range(N)]
    T = [input() for i in range(N)]
    # 90度回転
    def rotate(S):
        return ["".join([S[N-1-j][i] for j in range(N)]) for i in range(N)]
    # 90度回転
    def rotate_90(S):
        return ["".join([S[j][N-1-i] for j in range(N)]) for i in range(N)]
    # 180度回転
    def rotate_180(S):
        return ["".join([S[N-1-j][N-1-i] for j in range(N)]) for i in range(N)]
    # 270度回転
    def rotate_270(S):
        return ["".join([S[N-1-j][i] for j in range(N)]) for i in range(N)]
    # 横軸反転
    def flip(S):
        return ["".join([S[N-1-j][i] for j in range(N)]) for i in range(N)]
    # 縦軸反転
    def flip_vertical(S):
        return ["".join([S[j][N-1-i] for j in range(N)]) for i in range(N)]
    # 横軸反転
    def flip_horizontal(S):
        return ["".join([S[j][i] for j in range(N)]) for i in range(N)]
    # 90度回転
    def rotate(S):
        return ["".join([S[N-1-j][i] for j in range(N)]) for i in range(N)]
    # 90度回転
    def rotate_90(S):
        return ["".join([S[j][N-1-i] for j in range(N)]) for i in range(N)]
    # 180度回転
    def rotate_180(S):
        return ["".join([S[N-1-j][N-1-i] for j in range(N)]) for i in range(N)]
    # 270度回転
    def rotate_270(S):
        return ["".join([S[N-1-j][i] for j in
