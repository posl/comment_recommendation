def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    intervals.sort(key=lambda x: x[1])
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][2] >= intervals[j][1]:
                count += 1
    print(count)
