def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(M)]
    city.sort(key=lambda x: (x[0], x[1]))
    ans = [0] * M
    for i in range(M):
        ans[i] = str(city[i][0]).zfill(6) + str(i+1).zfill(6)
    print('
'.join(ans))
