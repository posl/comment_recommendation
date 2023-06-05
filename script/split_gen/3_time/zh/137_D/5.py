def main():
    n,m = map(int, input().split())
    data = [tuple(map(int, input().split())) for i in range(n)]
    data.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while m > 0:
        if i < n and data[i][0] <= m:
            ans += data[i][1]
            m -= data[i][0]
            i += 1
        else:
            break
    print(ans)
