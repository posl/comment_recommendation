def main():
    n = int(input())
    txa = [list(map(int, input().split())) for i in range(n)]
    #print(txa)
    txa.sort()
    #print(txa)
    t0, x0, a0 = 0, 0, 0
    ans = 0
    for t, x, a in txa:
        dt = t - t0
        dx = abs(x - x0)
        if dt < dx:
            print('No')
            return
        if (dt - dx) % 2 == 1:
            print('No')
            return
        m = (dt - dx) // 2
        ans += max(a, a0) + m
        t0, x0, a0 = t, x, a
    print(ans)

if __name__ == '__main__':
    main()