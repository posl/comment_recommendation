def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs = sorted(jobs, key=lambda x: x[0])
    reward = 0
    days = 0
    while days < M:
        A, B = jobs.pop()
        if days + A > M:
            continue
        reward += B
        days += A
    print(reward)

if __name__ == '__main__':
    main()