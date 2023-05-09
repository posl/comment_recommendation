def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[0])
    day = 0
    reward = 0
    while day < M:
        max_reward = 0
        max_reward_index = -1
        for i, (a, b) in enumerate(jobs):
            if a <= day:
                continue
            if b > max_reward:
                max_reward = b
                max_reward_index = i
        if max_reward_index == -1:
            break
        reward += max_reward
        day += 1
        del jobs[max_reward_index]
    print(reward)
