def main():
    N, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        ans += data[i][2] * (data[i][1] - data[i][0] + 1)
    for i in range(N):
        for j in range(i + 1, N):
            if data[i][1] < data[j][0]:
                break
            if data[i][1] <= data[j][1]:
                ans -= min(C, data[i][2]) * (data[i][1] - data[j][0] + 1)
            else:
                ans -= min(C, data[i][2]) * (data[j][1] - data[j][0] + 1)
    print(ans)

if __name__ == '__main__':
    main()