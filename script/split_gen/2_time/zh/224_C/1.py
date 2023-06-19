def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                x1 = x[i] - x[k]
                y1 = y[i] - y[k]
                x2 = x[j] - x[k]
                y2 = y[j] - y[k]
                if x1 * y2 - x2 * y1 != 0:
                    ans += 1
    print(ans // 6)
