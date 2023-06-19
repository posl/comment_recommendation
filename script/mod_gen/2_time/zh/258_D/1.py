def get_min_time(n, x, a_list, b_list):
    min_time = 0
    for i in range(n):
        if i == 0:
            min_time += a_list[i] + b_list[i]
        else:
            min_time += a_list[i]
    return min_time

if __name__ == '__main__':
    get_min_time()