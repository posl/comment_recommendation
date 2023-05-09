def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            tmp = 0
            for k in range(h):
                for l in range(w):
                    tmp = max(tmp, a[i][j] + a[k][l] - c * (i - k + j - l))
            ans = min(ans, tmp)
    print(ans)
