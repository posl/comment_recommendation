def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        a, b = map(int, input().split())
        jobs.append([a, b])
    jobs.sort()
    total = 0
    days = 0
    while days < M:
        max_reward = 0
        max_reward_index = 0
        for i in range(len(jobs)):
            if jobs[i][0] <= days:
                if jobs[i][1] > max_reward:
                    max_reward = jobs[i][1]
                    max_reward_index = i
            else:
                break
        if max_reward > 0:
            total += max_reward
            del jobs[max_reward_index]
        days += 1
    print(total)

if __name__ == '__main__':
    main()