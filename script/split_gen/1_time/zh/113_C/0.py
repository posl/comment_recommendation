def main():
    n, m = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(m)]
    data.sort(key=lambda x: x[1])
    cnt = [0] * (n + 1)
    for p, y in data:
        cnt[p] += 1
    ans = {}
    for p, y in data:
        ans[y] = (str(p).zfill(6) + str(cnt[p]).zfill(6))
        cnt[p] -= 1
    for p, y in data:
        print(ans[y])
