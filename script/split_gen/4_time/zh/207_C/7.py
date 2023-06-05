def main():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r - 0.5])
        elif t == 3:
            intervals.append([l + 0.5, r])
        else:
            intervals.append([l + 0.5, r - 0.5])
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[i][0] <= intervals[j][0] <= intervals[i][1] or intervals[j][0] <= intervals[i][0] <= intervals[j][1]:
                result += 1
    print(result)
