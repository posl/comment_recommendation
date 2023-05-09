def get_intervals():
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    return intervals
