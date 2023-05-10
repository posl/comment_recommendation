def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (points[i][0]-points[j][0])*(points[i][1]-points[k][1]) == (points[i][0]-points[k][0])*(points[i][1]-points[j][1]):
                    print("Yes")
                    exit()
    print("No")
