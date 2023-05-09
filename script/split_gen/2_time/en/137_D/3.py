def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    ans = 0
    reward = 0
    for A, B in jobs:
        if A <= M:
            reward += B
            M -= A
            ans = max(ans, reward)
    print(ans)
