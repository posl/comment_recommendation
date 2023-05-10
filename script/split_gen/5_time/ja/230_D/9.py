def main():
    n, d = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(n)]
    lrs.sort(key=lambda x: x[0])
    r = 0
    ans = 0
    for l, r in lrs:
        if r - l + 1 > d:
            ans += (r - l) // d
    print(ans)
