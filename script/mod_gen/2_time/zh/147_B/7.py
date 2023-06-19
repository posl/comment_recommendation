def get_min_hug_times(str):
    hug_times = 0
    for i in range(len(str)):
        if str[i] != str[len(str)-1-i]:
            hug_times += 1
    return hug_times // 2

if __name__ == '__main__':
    get_min_hug_times()