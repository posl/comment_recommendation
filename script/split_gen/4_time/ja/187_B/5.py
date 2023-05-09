def main():
    n = int(input())
    x_y = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (x_y[i][1] - x_y[j][1]) / (x_y[i][0] - x_y[j][0]) <= 1:
                cnt += 1
    print(cnt)
