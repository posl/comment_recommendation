def s(n):
    if n == 1:
        return [1]
    else:
        s_n_1 = s(n-1)
        return s_n_1 + [n] + s_n_1

if __name__ == '__main__':
    s()