def permutation(N, P):
    # 順列のリストを作成
    # 例：N = 3 なら
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    perm_list = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if j in perm_list:
                continue
            for k in range(1, N + 1):
                if k in perm_list:
                    continue
                perm_list.append([i, j, k])
    #print(perm_list)
    # P が何番目かを求める
    perm_list.sort()
    #print(perm_list)
    for i in range(len(perm_list)):
        if perm_list[i] == P:
            return perm_list[i - 1]
