def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    ans = []
    L, R = intervals[0]
    for l, r in intervals:
        if R < l:
            ans.append((L, R))
            L, R = l, r
        else:
            R = max(R, r)
    ans.append((L, R))
    print(len(ans))
    for L, R in ans:
        print(L, R)

if __name__ == '__main__':
    main()