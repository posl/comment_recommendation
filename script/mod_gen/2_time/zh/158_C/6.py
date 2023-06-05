def cal_balls(n, a, b):
    if n == 0:
        return 0
    if n == 1:
        return a
    if n == 2:
        return a + b
    return cal_balls(n - 1, a, b) + cal_balls(n - 2, a, b)

if __name__ == '__main__':
    cal_balls()