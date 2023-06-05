def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    max_reward = 0
    for job in jobs:
        if M > 0:
            max_reward += job[1]
            M -= 1
        else:
            break
    print(max_reward)
