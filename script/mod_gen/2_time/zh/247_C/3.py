def get_sn(n):
    if n == 1:
        return [1]
    else:
        sn_1 = get_sn(n-1)
        return sn_1 + [n] + sn_1

if __name__ == '__main__':
    get_sn()