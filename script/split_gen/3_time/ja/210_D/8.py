def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for j in range(w):
        for i in range(h):
            for k in range(w):
                for l in range(h):
                    if (i, j) != (l, k):
                        ans = min(ans, a[i][j] + a[l][k] + c * (abs(i - l) + abs(j - k)))
    print(ans)
