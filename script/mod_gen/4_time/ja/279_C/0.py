def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    #a = int(input())
    # スペース区切りの整数の入力
    #b, c = map(int, input().split())
    # 文字列の入力
    #s = input()
    # 出力
    #print("{} {}".format(a+b+c, s))
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    #print(S)
    #print(T)
    S_count = []
    for i in range(W):
        S_count.append([0,0])
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                S_count[j][0] += 1
            else:
                S_count[j][1] += 1
    #print(S_count)
    T_count = []
    for i in range(W):
        T_count.append([0,0])
    for i in range(H):
        for j in range(W):
            if T[i][j] == "#":
                T_count[j][0] += 1
            else:
                T_count[j][1] += 1
    #print(T_count)
    S_count.sort()
    T_count.sort()
    #print(S_count)
    #print(T_count)
    for i in range(W):
        if S_count[i] != T_count[i]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    solve()