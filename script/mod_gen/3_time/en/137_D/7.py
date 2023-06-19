def solve(n, m, jobs):
    jobs.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if m >= jobs[i][0]:
            ans += jobs[i][1]
            m -= 1
    return ans
n, m = map(int, input().split())
jobs = []
for i in range(n):
    a, b = map(int, input().split())
    jobs.append([a, b])
print(solve(n, m, jobs))
