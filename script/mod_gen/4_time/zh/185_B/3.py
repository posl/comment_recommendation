def solve(N, M, T, AB):
    # 电池电量
    battery = N
    # 离开家的时间
    leave = 0
    # 咖啡馆的下标
    index = 0
    # 咖啡馆的个数
    len_ab = len(AB)
    for t in range(1, T + 1):
        # 如果电量为0，返回No
        if battery == 0:
            return "No"
        # 如果时间为整数，电量减少1
        if t % 1 == 0:
            battery -= 1
        # 如果时间为半整数，电量增加1，如果电量为N，不增加
        if t % 0.5 == 0:
            if battery < N:
                battery += 1
        # 如果到达了咖啡馆，电量增加到N
        if index < len_ab and t == AB[index][0]:
            battery = N
            index += 1
        # 如果到达了回家的时间，电量减少到1
        if t == T:
            battery = 1
    # 如果电量为0，返回No
    if battery == 0:
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
    solve()