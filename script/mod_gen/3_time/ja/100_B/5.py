def cal_100(d, n):
    if d == 0:
        return n
    elif d == 1:
        return 100 * n
    else:
        return 10000 * n
d, n = map(int, input().split())
print(cal_100(d, n))

if __name__ == '__main__':
    cal_100()