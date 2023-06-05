def main():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = float('inf')
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l)))
    print(ans)
