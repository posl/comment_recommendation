def get_max_comfortable():
    player_num = int(input())
    player_list = list(map(int, input().split()))
    player_list.sort(reverse=True)
    total_comfortable = 0
    for i in range(player_num):
        if i == 0:
            total_comfortable += 0
        elif i == 1:
            total_comfortable += player_list[1]
        elif i == 2:
            total_comfortable += player_list[2]
        else:
            total_comfortable += player_list[i] + player_list[i-3]
    return total_comfortable
