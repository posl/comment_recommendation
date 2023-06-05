def get_inner_grade(n, r):
    if n < 10:
        return r + 100 * (10 - n)
    else:
        return r

if __name__ == '__main__':
    get_inner_grade()