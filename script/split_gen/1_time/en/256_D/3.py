def get_input():
    N = int(input())
    intervals = []
    for _ in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    return N, intervals
