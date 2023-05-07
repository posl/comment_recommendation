def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    p_y = sorted(zip(p, y, range(m)))
    r = [0] * m
    c = [0] * (n + 1)
    for i in range(m):
        c[p_y[i][0]] += 1
        r[p_y[i][2]] = '{:06}{:06}'.format(p_y[i][0], c[p_y[i][0]])
    print('
'.join(r))

if __name__ == '__main__':
    main()