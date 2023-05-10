def main():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort()
    for i in range(n):
        count = 0
        for j in range(m):
            if roads[j][0] == i + 1:
                count += 1
        print(count, end = " ")
        for j in range(m):
            if roads[j][0] == i + 1:
                print(roads[j][1], end = " ")
        print("")

if __name__ == '__main__':
    main()