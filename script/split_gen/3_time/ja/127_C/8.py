def main():
    n, m = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(m)]
    lrs.sort(key=lambda x: x[1])
    ans = 0
    r = 0
    for l, r in lrs:
        if r <= r:
            continue
        else:
            r = r
            ans += 1
    print(ans)
