def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intersect(intervals[i], intervals[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()