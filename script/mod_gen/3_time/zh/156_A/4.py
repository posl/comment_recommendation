def get_inner_score(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

if __name__ == '__main__':
    get_inner_score()