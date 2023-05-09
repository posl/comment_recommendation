def main():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r - 0.1])
        elif t == 3:
            intervals.append([l + 0.1, r])
        elif t == 4:
            intervals.append([l + 0.1, r - 0.1])
    intervals.sort(key=lambda x: x[0])
    #print(intervals)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if intervals[i][1] >= intervals[j][0]:
                count += 1
    print(count)
