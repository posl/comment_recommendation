def main():
    n, m = map(int, input().split())
    citys = []
    for i in range(m):
        p, y = map(int, input().split())
        citys.append([i, p, y])
    citys.sort(key=lambda x: (x[1], x[2]))
    ans = {}
    for i in range(m):
        ans[citys[i][0]] = str(citys[i][1]).zfill(6) + str(i + 1).zfill(6)
    for i in range(m):
        print(ans[i])

if __name__ == '__main__':
    main()