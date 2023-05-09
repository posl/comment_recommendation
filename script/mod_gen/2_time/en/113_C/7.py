def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        city.append(list(map(int, input().split())))
    city.sort(key=lambda x: x[1])
    ans = []
    for i in range(M):
        ans.append(str(city[i][0]).zfill(6) + str(i + 1).zfill(6))
    ans.sort(key=lambda x: int(x[:6]))
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()