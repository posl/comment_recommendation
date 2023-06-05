def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    #print(jobs)
    reward = 0
    while M > 0:
        max_reward = 0
        max_reward_idx = -1
        for i in range(len(jobs)):
            if jobs[i][0] <= M and jobs[i][1] > max_reward:
                max_reward = jobs[i][1]
                max_reward_idx = i
        if max_reward_idx >= 0:
            reward += max_reward
            M -= jobs[max_reward_idx][0]
            del jobs[max_reward_idx]
        else:
            break
    print(reward)

if __name__ == '__main__':
    main()