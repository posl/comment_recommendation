def run():
    a, b, c, d, e, f, x = map(int, input().split())
    t = 0
    p = 0
    while True:
        if t == x:
            print('draw')
            break
        t += 1
        if t % (a + b) <= a:
            p += d
        if t % (c + d) <= c:
            p -= e
        if p <= 0:
            print('takahashi')
            break
        if p > 0:
            print('aoki')
            break
