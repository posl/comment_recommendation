def main():
    n, m = map(int, input().split())
    jobs = [tuple(map(int, input().split())) for _ in range(n)]
    jobs.sort(key=lambda x: x[0])
    # print(jobs)
    ans = 0
    for i in range(m):
        if len(jobs) == 0:
            break
        max_reward = 0
        max_reward_index = -1
        for j in range(len(jobs)):
            if jobs[j][0] <= i + 1 and max_reward < jobs[j][1]:
                max_reward = jobs[j][1]
                max_reward_index = j
            else:
                break
        if max_reward_index != -1:
            ans += max_reward
            jobs.pop(max_reward_index)
    print(ans)

if __name__ == '__main__':
    main()