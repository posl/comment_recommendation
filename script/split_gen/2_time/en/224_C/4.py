def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                a = points[i][0] - points[j][0]
                b = points[i][1] - points[j][1]
                c = points[k][0] - points[j][0]
                d = points[k][1] - points[j][1]
                if a*d != b*c:
                    count += 1
    print(count)
