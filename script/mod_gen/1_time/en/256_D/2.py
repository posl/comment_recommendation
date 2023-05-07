def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    ans = []
    L, R = intervals[0]
    for i in range(1,N):
        if R < intervals[i][0]:
            ans.append((L, R))
            L, R = intervals[i]
        else:
            R = max(R, intervals[i][1])
    ans.append((L, R))
    for i in ans:
        print(i[0], i[1])

if __name__ == '__main__':
    main()