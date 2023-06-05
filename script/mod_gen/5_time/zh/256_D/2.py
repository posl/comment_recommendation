def main():
    n = int(input())
    intervals = list()
    for i in range(n):
        line = input().split()
        intervals.append((int(line[0]), int(line[1])))
    intervals.sort(key=lambda x: x[0])
    tmp = intervals[0]
    ans = list()
    for i in range(1, n):
        if tmp[1] >= intervals[i][0]:
            tmp = (tmp[0], max(tmp[1], intervals[i][1]))
        else:
            ans.append(tmp)
            tmp = intervals[i]
    ans.append(tmp)
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]))

if __name__ == '__main__':
    main()