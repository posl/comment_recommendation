def get_comma_cnt(n):
    comma_cnt = 0
    n_str = str(n)
    n_len = len(n_str)
    for i in range(n_len):
        if i % 3 == 0 and i != 0:
            comma_cnt += 1
    return comma_cnt

if __name__ == '__main__':
    get_comma_cnt()