def check_path(n, m, path):
    # チェック用の配列を作成
    check_list = [0 for i in range(n+1)]
    # 部屋1から出発して、部屋1に戻れるかチェックする
    check_list[1] = 1
    for i in range(m):
        if path[i][0] == 1:
            check_list[path[i][1]] = 1
        elif path[i][1] == 1:
            check_list[path[i][0]] = 1
    for i in range(m):
        if check_list[path[i][0]] == 1:
            check_list[path[i][1]] = 1
        elif check_list[path[i][1]] == 1:
            check_list[path[i][0]] = 1
    for i in range(2, n+1):
        if check_list[i] == 0:
            return False
    return True
