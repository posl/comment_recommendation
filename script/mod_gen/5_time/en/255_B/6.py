def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    def check(r):
        for i in range(N):
            x, y = XY[i]
            for j in range(i+1, N):
                x2, y2 = XY[j]
                if (x2-x)**2 + (y2-y)**2 <= r**2:
                    break
            else:
                return False
        return True
    l = 0
    r = 10**9
    while r - l > 1e-5:
        m = (l+r)/2
        if check(m):
            r = m
        else:
            l = m
    print(r)

if __name__ == '__main__':
    main()