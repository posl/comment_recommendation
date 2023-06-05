def main():
    a, b, c, d, e, f, x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x:
            print('draw')
            break
        taka += a
        if taka >= x:
            print('taka')
            break
        aoki += d
        if aoki >= x:
            print('aoki')
            break
        taka += b
        aoki += e
        if taka >= x:
            print('taka')
            break
        aoki += f
