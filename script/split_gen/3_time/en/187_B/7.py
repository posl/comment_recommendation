def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(points[i][1]-points[j][1]) <= abs(points[i][0]-points[j][0]):
                count += 1
    print(count)
main()
# AC
