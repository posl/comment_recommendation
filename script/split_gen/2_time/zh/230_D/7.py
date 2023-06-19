def main():
    n, d = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[1])
    r = 0
    ans = 0
    for l, r in lr:
        if r - l + 1 <= d:
            continue
        ans += (r - l + 1 - d) // d
        if (r - l + 1 - d) % d != 0:
            ans += 1
    print(ans)
