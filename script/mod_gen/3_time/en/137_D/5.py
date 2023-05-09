def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    days = 0
    for job in jobs:
        if days + job[0] <= M:
            ans += job[1]
            days += job[0]
    print(ans)

if __name__ == '__main__':
    main()