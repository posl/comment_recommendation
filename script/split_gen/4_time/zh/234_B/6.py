def get_max_dis(points):
    max_dis = 0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            dis = ((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)**0.5
            if dis > max_dis:
                max_dis = dis
    return max_dis
