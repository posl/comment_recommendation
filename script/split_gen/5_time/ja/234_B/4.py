def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
N = int(input())
point_list = []
for i in range(N):
    point_list.append(list(map(int, input().split())))
max_distance = 0
for i in range(N):
    for j in range(i+1, N):
        distance = get_distance(point_list[i][0], point_list[i][1], point_list[j][0], point_list[j][1])
        if distance > max_distance:
            max_distance = distance
print(max_distance)
