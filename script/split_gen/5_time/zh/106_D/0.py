def find_train_num(citys, trains, querys):
    # citys: 城市数目
    # trains: 列车数目
    # querys: 查询数目
    # trains_list: 列车列表
    # querys_list: 查询列表
    trains_list = []
    querys_list = []
    for i in range(trains):
        trains_list.append(list(map(int, input().split())))
    for j in range(querys):
        querys_list.append(list(map(int, input().split())))
    for k in range(querys):
        count = 0
        for l in range(trains):
            if querys_list[k][0] <= trains_list[l][0] and trains_list[l][1] <= querys_list[k][1]:
                count += 1
        print(count)
