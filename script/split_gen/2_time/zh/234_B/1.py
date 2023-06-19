def main():
    #读取输入
    n = int(input())
    points = []
    for i in range(n):
        x = int(input().split()[0])
        y = int(input().split()[1])
        points.append((x, y))
    #计算最大距离
    max_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
            if dist > max_dist:
                max_dist = dist
    #输出结果
    print(max_dist)
