def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    # SとTの#の位置をリスト化
    S_list = []
    T_list = []
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                S_list.append([i, j])
            if T[i][j] == "#":
                T_list.append([i, j])
    # 回転と移動を行う
    for _ in range(4):
        # Tを回転させる
        T_list = [[T_list[i][1], N - 1 - T_list[i][0]] for i in range(len(T_list))]
        # Tを移動させる
        T_list = [[T_list[i][0] - S_list[0][0] + T_list[0][0], T_list[i][1] - S_list[0][1] + T_list[0][1]] for i in range(len(T_list))]
        # SとTの#の位置が一致するか判定
        if sorted(S_list) == sorted(T_list):
            print("Yes")
            return
    print("No")
