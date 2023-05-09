def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    ans = []
    for l, r in intervals:
        if not ans:
            ans.append((l, r))
            continue
        if ans[-1][1] >= r:
            continue
        if ans[-1][1] >= l:
            ans[-1] = (ans[-1][0], r)
            continue
        ans.append((l, r))
    for l, r in ans:
        print(l, r)

if __name__ == '__main__':
    main()