def print_road(n, m, road):
    road = sorted(road, key=lambda x: x[0])
    for i in range(n):
        res = [0]
        for j in range(m):
            if road[j][0] == i+1:
                res.append(road[j][1])
        print(len(res)-1, end=' ')
        print(*res[1:])

if __name__ == '__main__':
    print_road()