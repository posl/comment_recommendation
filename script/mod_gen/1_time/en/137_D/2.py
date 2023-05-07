def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        jobs.append(tuple(map(int, input().split())))
    jobs.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    i = 0
    while i < N and jobs[i][1] > 0:
        if M - jobs[i][0] >= 0:
            M -= jobs[i][0]
            ans += jobs[i][1]
        else:
            break
        i += 1
    print(ans)

if __name__ == '__main__':
    main()