def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i + j))
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] - c * (i + j))
    print(ans)
