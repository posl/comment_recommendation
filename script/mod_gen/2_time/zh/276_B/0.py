def get_city_num(n, m, road_list):
    city_num_list = [0 for i in range(n)]
    for road in road_list:
        city_num_list[road[0] - 1] += 1
        city_num_list[road[1] - 1] += 1
    return city_num_list

if __name__ == '__main__':
    get_city_num()