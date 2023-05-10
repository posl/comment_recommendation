def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    ans = 0
    for i in range(N):
        A, B = jobs[i]
        if A > M:
            break
        ans += B
        M -= A
    print(ans)
