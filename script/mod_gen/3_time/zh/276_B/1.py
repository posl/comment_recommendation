def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    roads.sort(key=lambda x: x[1])
    roads.sort(key=lambda x: x[0])
    roads = [[roads[0][0], roads[0][1], 1]]
    for i in range(1, m):
        if roads[-1][0] == roads[i][0]:
            if roads[-1][1] == roads[i][1] - 1:
                roads[-1][2] += 1
            else:
                roads.append([roads[i][0], roads[i][1], 1])
        else:
            roads.append([roads[i][0], roads[i][1], 1])
    i, j = 0, 0
    while i < n:
        if j < len(roads) and roads[j][0] == i + 1:
            print(roads[j][2], *range(roads[j][1] - roads[j][2] + 1, roads[j][1] + 1))
            j += 1
        else:
            print(0)
        i += 1

if __name__ == '__main__':
    main()