def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    #print(jobs)
    ans = 0
    j = 0
    for i in range(1, M+1):
        while j < N and jobs[j][0] <= i:
            j += 1
        if j > 0:
            ans += jobs[j-1][1]
    print(ans)

if __name__ == '__main__':
    main()