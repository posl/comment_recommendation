def main():
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]
    data.sort()
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (data[j][1] - data[i][1]) / (data[j][0] - data[i][0]) <= 1:
                cnt += 1
    print(cnt)
