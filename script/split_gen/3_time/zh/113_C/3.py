def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        P, Y = map(int, input().split())
        city.append([P, Y, i])
    city.sort(key=lambda x: x[1])
    count = [0] * (N + 1)
    ans = []
    for i in range(M):
        count[city[i][0]] += 1
        ans.append([city[i][0], count[city[i][0]], city[i][2]])
    ans.sort(key=lambda x: x[2])
    for i in range(M):
        print(str(ans[i][0]).zfill(6) + str(ans[i][1]).zfill(6))
