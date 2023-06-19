def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()
    from collections import deque
    dq = deque()
    ans = 0
    i = 0
    for day in range(1, m + 1):
        while i < n and jobs[i][0] <= day:
            dq.append(jobs[i][1])
            i += 1
        if dq:
            ans += dq.pop()
    print(ans)
