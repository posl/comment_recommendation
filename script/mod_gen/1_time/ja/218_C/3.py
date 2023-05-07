def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    # S = [list(input()) for _ in range(N)]
    # T = [list(input()) for _ in range(N)]
    # Sの#の集合
    S_set = set()
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                S_set.add((i, j))
    # Tの#の集合
    T_set = set()
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                T_set.add((i, j))
    # Sの#の集合の中心
    S_center = (0, 0)
    for i, j in S_set:
        S_center = (S_center[0] + i, S_center[1] + j)
    S_center = (S_center[0] // len(S_set), S_center[1] // len(S_set))
    # Tの#の集合の中心
    T_center = (0, 0)
    for i, j in T_set:
        T_center = (T_center[0] + i, T_center[1] + j)
    T_center = (T_center[0] // len(T_set), T_center[1] // len(T_set))
    # Sの#の集合の中心とTの#の集合の中心をずらしたときの、Sの#の集合の中心とTの#の集合の中心の差
    diff = (T_center[0] - S_center[0], T_center[1] - S_center[1])
    # Sの#の集合の中心とTの#の集合の中心をずらしたときの、Sの#の集合の中心とTの#の集合の中心の差の絶対値
    abs_diff = (abs(T_center[0] - S_center[0]), abs(T_center[1] - S_center[1]))
    # Sの#の集合の中心とTの#の集合の中心を

if __name__ == '__main__':
    main()