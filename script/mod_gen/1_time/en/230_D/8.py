def main():
    import sys
    readline = sys.stdin.readline
    N, D = map(int, readline().split())
    LR = [list(map(int, readline().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = 0
    r = -1
    for l, r in LR:
        if r <= r:
            continue
        ans += -(-((r - l) // D))
        r = l + D * ans
    print(ans)

if __name__ == '__main__':
    main()