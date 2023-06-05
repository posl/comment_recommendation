def main():
    num = int(input())
    points = []
    for i in range(num):
        points.append([int(x) for x in input().split()])
    #print(points)
    for i in range(num):
        for j in range(i+1,num):
            for k in range(j+1,num):
                if (points[i][0]-points[j][0])*(points[j][1]-points[k][1]) == (points[j][0]-points[k][0])*(points[i][1]-points[j][1]):
                    print("Yes")
                    return
    print("No")
    return
