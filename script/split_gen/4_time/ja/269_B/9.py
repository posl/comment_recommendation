def main():
    # input
    S = []
    for _ in range(10):
        S.append(input())
    # compute
    # まず、Sを10個のリストに分割する
    S_list = []
    for i in range(10):
        S_list.append(list(S[i]))
    # 1行目の#の位置を探す
    for i in range(10):
        if S_list[0][i] == '#':
            A = i + 1
            break
    # 10行目の#の位置を探す
    for i in range(10):
        if S_list[9][i] == '#':
            B = i + 1
            break
    # 1列目の#の位置を探す
    for i in range(10):
        if S_list[i][0] == '#':
            C = i + 1
            break
    # 10列目の#の位置を探す
    for i in range(10):
        if S_list[i][9] == '#':
            D = i + 1
            break
    # output
    print(A, B)
    print(C, D)
