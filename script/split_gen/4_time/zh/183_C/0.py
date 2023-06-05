def get_city_list(city_num):
    if city_num == 1:
        return [1]
    city_list = []
    for i in range(1, city_num+1):
        city_list.append(i)
    return city_list
