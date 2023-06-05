def get_min_max(s):
    min_str = s
    max_str = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_str:
            min_str = s
        if s > max_str:
            max_str = s
    return min_str, max_str

if __name__ == '__main__':
    get_min_max()