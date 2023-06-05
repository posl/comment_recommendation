def get_next_confusing_time(time):
    h = time[0]
    m = time[1]
    if m == 59:
        if h == 23:
            return [0, 0]
        else:
            return [h + 1, 0]
    else:
        return [h, m + 1]

if __name__ == '__main__':
    get_next_confusing_time()