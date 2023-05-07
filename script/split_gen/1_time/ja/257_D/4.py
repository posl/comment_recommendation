def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans = max(ans, (abs(data[i][0] - data[j][0]) + abs(data[i][1] - data[j][1])) / data[i][2])
    print(math.ceil(ans))
