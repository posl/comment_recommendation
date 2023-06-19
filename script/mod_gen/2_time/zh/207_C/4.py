def count_intersection(n, intervals):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if intervals[i][0] < intervals[j][0] < intervals[i][1] < intervals[j][1]:
                cnt += 1
            elif intervals[j][0] < intervals[i][0] < intervals[j][1] < intervals[i][1]:
                cnt += 1
    return cnt

if __name__ == '__main__':
    count_intersection()