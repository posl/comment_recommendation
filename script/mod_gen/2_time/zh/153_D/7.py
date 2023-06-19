def get_min_attack_times(h):
    if h == 1:
        return 1
    elif h == 2:
        return 3
    else:
        i = 0
        while h > 0:
            i += 1
            h = h // 2
        return 2 ** i - 1

if __name__ == '__main__':
    get_min_attack_times()