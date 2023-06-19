def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    import bisect
    for i in range(q):
        ans = 10**20
        for shrine in [s[bisect.bisect_left(s, x[i]) - 1], s[bisect.bisect_right(s, x[i]) - 1]]:
            for temple in [t[bisect.bisect_left(t, x[i]) - 1], t[bisect.bisect_right(t, x[i]) - 1]]:
                d = abs(shrine - x[i]) + abs(shrine - temple)
                ans = min(ans, d)
                d = abs(temple - x[i]) + abs(temple - shrine)
                ans = min(ans, d)
        print(ans)

if __name__ == '__main__':
    main()