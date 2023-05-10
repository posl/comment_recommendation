def main():
    import sys
    import math
    n = int(sys.stdin.readline().strip())
    points = []
    for i in range(n):
        x,y = map(int,sys.stdin.readline().strip().split())
        points.append([x,y])
    max_distance = 0
    for i in range(n):
        for j in range(i+1,n):
            distance = math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
            if distance > max_distance:
                max_distance = distance
    print(max_distance)
