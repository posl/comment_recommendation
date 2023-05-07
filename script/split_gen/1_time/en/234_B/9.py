def main():
    import math
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int,input().split())))
    #print(points)
    max_distance = 0
    for i in range(N):
        for j in range(i+1,N):
            distance = math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
            if distance > max_distance:
                max_distance = distance
    print(max_distance)
