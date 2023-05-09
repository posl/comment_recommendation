def main():
    n, d = map(int, input().split())
    x = []
    y = []
    for _ in range(n):
        tmp_x, tmp_y = map(int, input().split())
        x.append(tmp_x)
        y.append(tmp_y)
    cnt = 0
    for i in range(n):
        if x[i]**2 + y[i]**2 <= d**2:
            cnt += 1
    print(cnt)
