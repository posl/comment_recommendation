def get_num(n):
    if n < 11:
        return 0
    else:
        n = str(n)
        n_len = len(n)
        if n_len % 2 == 0:
            half_len = int(n_len / 2)
            half_n = n[0:half_len]
            half_n2 = n[half_len:n_len]
            if half_n <= half_n2:
                return int(half_n) - 1
            else:
                return int(half_n) - 2
        else:
            half_len = int((n_len + 1) / 2)
            half_n = n[0:half_len]
            half_n2 = n[half_len:n_len]
            if half_n <= half_n2:
                return int(half_n) - 1
            else:
                return int(half_n) - 2
