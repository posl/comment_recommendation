def find_max_floor(N, ladders):
    # print(N, ladders)
    if N == 1:
        return 1
    # ladders = sorted(ladders, key=lambda x: x[0])
    # print(ladders)
    # max_floor = 1
    # for i in range(len(ladders)):
    #     if ladders[i][0] > max_floor:
    #         return max_floor
    #     else:
    #         max_floor = max(max_floor, ladders[i][1])
    # return max_floor
    max_floor = 1
    ladders = sorted(ladders, key=lambda x: x[1])
    for i in range(len(ladders)):
        if ladders[i][1] > max_floor:
            return max_floor
        else:
            max_floor = max(max_floor, ladders[i][0])
    return max_floor
