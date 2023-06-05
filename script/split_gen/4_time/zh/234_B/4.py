def main():
    N = int(input())
    points = []
    for _ in range(N):
        point = input().split()
        point = [int(x) for x in point]
        points.append(point)
    max_dis = 0
    for i in range(N):
        for j in range(i+1, N):
            dis = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
            if dis > max_dis:
                max_dis = dis
    print(max_dis)
