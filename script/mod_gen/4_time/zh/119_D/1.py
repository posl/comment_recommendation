def get_min_dist(x, s, t):
    s_len = len(s)
    t_len = len(t)
    s_index = 0
    t_index = 0
    min_dist = 2**32
    while s_index < s_len and t_index < t_len:
        dist = abs(s[s_index] - x) + abs(t[t_index] - s[s_index])
        if dist < min_dist:
            min_dist = dist
        if s[s_index] < t[t_index]:
            s_index += 1
        else:
            t_index += 1
    while s_index < s_len:
        dist = abs(s[s_index] - x) + abs(t[-1] - s[s_index])
        if dist < min_dist:
            min_dist = dist
        s_index += 1
    while t_index < t_len:
        dist = abs(s[-1] - x) + abs(t[t_index] - s[-1])
        if dist < min_dist:
            min_dist = dist
        t_index += 1
    return min_dist

if __name__ == '__main__':
    get_min_dist()