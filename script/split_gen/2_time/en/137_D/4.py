def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort(key=lambda x: x[0])
    reward = 0
    jobs = []
    for i in range(N):
        if AB[i][0] <= M:
            reward += AB[i][1]
            jobs.append(AB[i][0])
            M -= 1
    jobs.sort()
    for i in range(len(jobs)):
        if jobs[i] <= M:
            reward -= 1
            M -= 1
    print(reward)
