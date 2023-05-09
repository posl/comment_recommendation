def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    ans = []
    left, right = intervals[0]
    for i in range(1, N):
        if right >= intervals[i][0]:
            right = max(right, intervals[i][1])
        else:
            ans.append((left, right))
            left, right = intervals[i]
    ans.append((left, right))
    for a in ans:
        print(*a)

if __name__ == '__main__':
    main()