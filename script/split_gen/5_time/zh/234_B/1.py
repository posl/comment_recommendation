def problem234_b():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            length = ((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)**0.5
            if length > max_length:
                max_length = length
    print(max_length)
problem234_b()
