def main():
    n, m = map(int, input().split())
    data = []
    for i in range(n):
        a, b = map(int, input().split())
        data.append([a, b])
    data = sorted(data, key=lambda x: x[0])
    ans = 0
    cnt = 0
    for i in range(n):
        if cnt + data[i][1] >= m:
            ans += data[i][0] * (m - cnt)
            break
        else:
            ans += data[i][0] * data[i][1]
            cnt += data[i][1]
    print(ans)
