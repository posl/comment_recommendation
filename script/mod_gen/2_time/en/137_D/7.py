def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)
    days = 0
    reward = 0
    for job in jobs:
        if days + job[0] <= M:
            days += job[0]
            reward += job[1]
    print(reward)

if __name__ == '__main__':
    main()