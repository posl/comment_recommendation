def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [min(a[i]) for i in range(h)]
    c = [min([a[i][j] for i in range(h)]) for j in range(w)]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += max(a[i][j] - b[i] - c[j], 0)
    print(ans)
