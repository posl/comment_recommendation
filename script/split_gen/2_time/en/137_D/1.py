def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs = sorted(jobs, key=lambda x: x[0])
    ans = 0
    reward = 0
    for i in range(N):
        A, B = jobs[i]
        reward += B
        if A <= M:
            ans = max(ans, reward)
        else:
            break
    print(ans)
