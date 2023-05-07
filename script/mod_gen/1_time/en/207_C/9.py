def main():
    N = int(input())
    #print(N)
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        #print(t, l, r)
        intervals.append((t, l, r))
    #print(intervals)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j)
            ans += intersect(intervals[i], intervals[j])
    print(ans)

if __name__ == '__main__':
    main()