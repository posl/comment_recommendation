def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    d = {}
    for j in range(1, m+1):
        while i < n and ab[i][0] <= j:
            if ab[i][1] in d:
                d[ab[i][1]] += 1
            else:
                d[ab[i][1]] = 1
            i += 1
        if d:
            k = max(d.keys())
            ans += k
            d[k] -= 1
            if d[k] == 0:
                del d[k]
    print(ans)
