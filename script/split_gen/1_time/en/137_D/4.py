def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    reward = 0
    for i in range(N):
        if jobs[i][0] <= M:
            reward += jobs[i][1]
            M -= jobs[i][0]
        else:
            break
    print(reward)
