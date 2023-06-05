def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            cnt = 0
            for k in range(n):
                for l in range(k+1, n):
                    if x[k] - x[l] == dx and y[k] - y[l] == dy:
                        cnt += 1
            ans = max(ans, n - cnt)
    print(ans)
