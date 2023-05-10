def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()
    jobs.reverse()
    days = []
    for i in range(m):
        days.append(i + 1)
    days.reverse()
    total = 0
    for i in range(m):
        for j in range(n):
            if jobs[j][0] <= days[i]:
                total += jobs[j][1]
                jobs.pop(j)
                break
    print(total)
