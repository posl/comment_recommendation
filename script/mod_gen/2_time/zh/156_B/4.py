def get_inner_score(n, r):
    return r + 100 * max(10 - n, 0)

if __name__ == '__main__':
    get_inner_score()