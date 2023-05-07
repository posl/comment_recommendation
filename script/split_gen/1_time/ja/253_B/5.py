def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    x = []
    y = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                x.append(i)
                y.append(j)
    ans = 10**9
    for i in range(h):
        for j in range(w):
            tmp = 0
            for k in range(2):
                tmp += abs(x[k] - i) + abs(y[k] - j)
            ans = min(ans, tmp)
    print(ans)
