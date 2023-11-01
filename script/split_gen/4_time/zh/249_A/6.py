def main():
    a, b, c, d, e, f, x = map(int, input().split())
    t = 0
    while x > 0:
        if t % (a + b) < a:
            x -= e
        else:
            x -= f
        if x <= 0:
            print('Takahashi')
            break
        if t % (c + d) < c:
            x -= e
        else:
            x -= f
        if x <= 0:
            print('Aoki')
