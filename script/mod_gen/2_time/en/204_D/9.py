def find_min_time(oven_list):
    oven_list.sort()
    if len(oven_list) == 1:
        return oven_list[0]
    elif len(oven_list) == 2:
        return oven_list[1]
    else:
        return oven_list[0] + find_min_time(oven_list[1:])

if __name__ == '__main__':
    find_min_time()