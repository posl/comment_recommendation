def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        jobs.append(tuple(map(int, input().split())))
    jobs.sort()
    jobs = jobs[::-1]
    day = m
    reward = 0
    while day > 0:
        max_reward = 0
        max_reward_index = -1
        for i in range(len(jobs)):
            if jobs[i][0] <= day:
                if jobs[i][1] > max_reward:
                    max_reward = jobs[i][1]
                    max_reward_index = i
        if max_reward_index > -1:
            reward += max_reward
            day -= 1
            jobs.pop(max_reward_index)
        else:
            break
    print(reward)
