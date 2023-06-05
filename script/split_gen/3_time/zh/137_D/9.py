def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key = lambda x:x[0])
    total = 0
    i = 0
    while m > 0 and i < n:
        if jobs[i][0] <= m:
            total += jobs[i][1]
            m -= jobs[i][0]
        i += 1
    print(total)
