def make_list(n):
    if n == 1:
        return [1]
    else:
        return make_list(n-1) + [n] + make_list(n-1)

if __name__ == '__main__':
    make_list()