def main():
    n, m = map(int, input().split())
    if n == 2:
        print(0)
        return
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[0])
    ans = 0
    for i in range(m):
        u, v = edges[i]
        if u == v:
            continue
        if i == 0:
            ans += n - v
        else:
            if edges[i - 1][1] < v:
                ans += n - v
            else:
                ans += edges[i - 1][1] - v
    print(ans)
