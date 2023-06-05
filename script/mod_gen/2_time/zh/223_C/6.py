def get_min_max_str(s):
    l = len(s)
    min_str = s
    max_str = s
    for i in range(l):
        tmp_str = s[i:] + s[:i]
        if tmp_str < min_str:
            min_str = tmp_str
        if tmp_str > max_str:
            max_str = tmp_str
    return min_str, max_str

if __name__ == '__main__':
    get_min_max_str()