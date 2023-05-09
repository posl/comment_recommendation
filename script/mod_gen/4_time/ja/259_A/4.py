def calc_height(m, x, t, d):
    height = t
    for i in range(x, m):
        height += d
    return height
n, m, x, t, d = map(int, input().split())
print(calc_height(m, x, t, d))

if __name__ == '__main__':
    calc_height()