def get_second_place_player(N, A):
    # 从小到大排序
    A.sort()
    # 用来存储每一轮的比赛结果
    match_list = []
    # 每一轮的比赛
    for i in range(N):
        # 比赛结果
        match_result = []
        # 比赛
        for j in range(2 ** (N - i - 1)):
            # 比赛结果
            match_result.append(max(A[2 * j], A[2 * j + 1]))
        # 比赛结果加入比赛列表
        match_list.append(match_result)
        # 更新A
        A = match_result
    # 打印第二名
    print(match_list[-2][1])

if __name__ == '__main__':
    get_second_place_player()