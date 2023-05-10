def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    # print(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # print(i, j, k)
                if (points[j][1]-points[i][1])*(points[k][0]-points[i][0]) == (points[k][1]-points[i][1])*(points[j][0]-points[i][0]):
                    print('Yes')
                    return
    print('No')
