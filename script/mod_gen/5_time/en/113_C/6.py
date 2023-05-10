def main():
    n, m = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(m)]
    cities = sorted(cities, key=lambda x: x[1])
    ans = []
    for i, city in enumerate(cities):
        ans.append([city[0], str(i+1).zfill(6)])
    ans = sorted(ans, key=lambda x: x[0])
    for a in ans:
        print(str(a[0]).zfill(6)+a[1])

if __name__ == '__main__':
    main()