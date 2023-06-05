def max_reward(n, m, jobs):
    jobs.sort(key=lambda x:x[1])
    ans = 0
    for i in range(m):
        if len(jobs) == 0:
            break
        ans += jobs.pop()[1]
    return ans
