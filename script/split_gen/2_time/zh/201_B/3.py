def get_second_height_mountain_number(n, height_list):
    height_list.sort(reverse=True)
    return height_list[1][0]
