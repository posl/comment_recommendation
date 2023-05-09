def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    l = 0
    r = 1000000
    while r - l > 1e-6:
        m = (r + l) / 2
        t = 0
        for a, b in AB:
            t += a / (m / b)
        if t >= 2:
            l = m
        else:
            r = m
    print(l)

if __name__ == '__main__':
    main()