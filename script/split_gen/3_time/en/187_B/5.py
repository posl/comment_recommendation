def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            slope = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
            if slope >= -1 and slope <= 1:
                count += 1
    print(count)
