def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    for i in range(n):
        t.append(list(map(int, input().split())))
    # print(s)
    # print(t)
    # print('-----------------------')
    # print(s[0][0], s[0][1])
    # print(s[1][0], s[1][1])
    # print(s[2][0], s[2][1])
    # print('-----------------------')
    # print(t[0][0], t[0][1])
    # print(t[1][0], t[1][1])
    # print(t[2][0], t[2][1])
    # print('-----------------------')
    p = 0
    while p < 360:
        q = t[0][0] - s[0][0]
        r = t[0][1] - s[0][1]
        # print('p=', p, 'q=', q, 'r=', r)
        i = 0
        while i < n:
            x = s[i][0] * math.cos(math.radians(p)) - s[i][1] * math.sin(math.radians(p)) + q
            y = s[i][0] * math.sin(math.radians(p)) + s[i][1] * math.cos(math.radians(p)) + r
            # print('i=', i, 'x=', x, 'y=', y)
            if t[i][0] != x or t[i][1] != y:
                # print('No')
                break
            i += 1
        if i == n:
            print('Yes')
            break
        p += 1
    if p == 360:
        print('No')

if __name__ == '__main__':
    main()