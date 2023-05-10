def problem287_b():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for si in s:
        for ti in t:
            if si[-3:] == ti:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    problem287_b()