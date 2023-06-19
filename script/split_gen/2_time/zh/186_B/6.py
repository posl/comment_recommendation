def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = 101
    for i in range(h):
        for j in range(w):
            if a[i][j] < min_a:
                min_a = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)
