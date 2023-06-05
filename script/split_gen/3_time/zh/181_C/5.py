def judge(points):
    for i in xrange(0, len(points)-2):
        for j in xrange(i+1, len(points)-1):
            for k in xrange(j+1, len(points)):
                if (points[i][0]-points[j][0])*(points[i][1]-points[k][1]) == \
                   (points[i][0]-points[k][0])*(points[i][1]-points[j][1]):
                    return True
    return False
