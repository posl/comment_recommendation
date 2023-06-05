def main():
    n, m = map(int, input().split())
    city = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        city[a-1].append(b)
        city[b-1].append(a)
    for i in range(n):
        city[i].sort()
        print(len(city[i]), end=' ')
        for j in range(len(city[i])):
            print(city[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()