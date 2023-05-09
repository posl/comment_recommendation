def main():
    n, m = map(int, input().split())
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))
    for i in range(n):
        count = 0
        for j in range(m):
            if road[j][0] == i+1 or road[j][1] == i+1:
                count += 1
        print(count)
