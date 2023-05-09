def solve():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)
    days = [0 for i in range(10**5+1)]
    for i in range(N):
        days[jobs[i][0]] += jobs[i][1]
    ans = 0
    for i in range(1, M+1):
        ans += days[i]
    print(ans)

if __name__ == '__main__':
    solve()