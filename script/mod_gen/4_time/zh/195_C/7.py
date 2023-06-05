def count_comma(n):
    n_str = str(n)
    n_len = len(n_str)
    if n_len < 4:
        return 0
    else:
        return n_len//3 - 1

if __name__ == '__main__':
    count_comma()