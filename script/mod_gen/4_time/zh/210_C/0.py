def get_max_color_num(N,K,c):
    max_num = 0
    for i in range(N-K+1):
        color_set = set(c[i:i+K])
        if len(color_set) > max_num:
            max_num = len(color_set)
    return max_num

if __name__ == '__main__':
    get_max_color_num()