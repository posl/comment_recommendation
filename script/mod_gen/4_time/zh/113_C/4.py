def main():
    n, m = map(int, input().split())
    city = []
    for i in range(m):
        p, y = map(int, input().split())
        city.append([i, p, y])
    city.sort(key=lambda x: x[2])
    ans = []
    for i in range(m):
        ans.append([city[i][0], city[i][1], i + 1])
    ans.sort(key=lambda x: x[0])
    for i in range(m):
        print(str(ans[i][1]).zfill(6) + str(ans[i][2]).zfill(6))

if __name__ == '__main__':
    main()