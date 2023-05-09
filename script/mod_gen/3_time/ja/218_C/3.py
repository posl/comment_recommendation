def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    # 90度回転
    def rotate(S):
        return ["".join([S[j][N-1-i] for j in range(N)]) for i in range(N)]
    # ずらす
    def shift(S, dx, dy):
        return ["".join([S[y][x] if 0 <= y+dy < N and 0 <= x+dx < N else "." for x in range(N)]) for y in range(N)]
    # 90度回転とずらす
    def rotate_and_shift(S, dx, dy):
        return shift(rotate(S), dx, dy)
    # ずらして90度回転
    def shift_and_rotate(S, dx, dy):
        return rotate(shift(S, dx, dy))
    # 一致判定
    def equal(S, T):
        return all([s == t for s, t in zip(S, T)])
    # ずらす
    for dx in range(N):
        for dy in range(N):
            # 90度回転とずらす
            if equal(rotate_and_shift(S, dx, dy), T):
                print("Yes")
                return
            # ずらして90度回転
            if equal(shift_and_rotate(S, dx, dy), T):
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()