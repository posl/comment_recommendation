def main():
    n, m = map(int, input().split())
    cities = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        cities[a-1].append(b)
        cities[b-1].append(a)
    for i in range(n):
        print(len(cities[i]), *sorted(cities[i]))

if __name__ == '__main__':
    main()