def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        P, Y = map(int, input().split())
        city.append([P, Y, i])
    city.sort(key=lambda x: x[1])
    ans = [None] * M
    for i in range(M):
        ans[city[i][2]] = '{:06}{:06}'.format(city[i][0], i + 1)
    for i in range(M):
        print(ans[i])
