def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    x = 0
    t = 0
    for i in range(n):
        x0, t0, a0 = txa[i]
        d = x0 - x
        dt = t0 - t
        if a0 > d + dt:
            print('No')
            return
        if a0 % 2 != (d + dt) % 2:
            print('No')
            return
        x = x0
        t = t0
    print('Yes')

if __name__ == '__main__':
    main()