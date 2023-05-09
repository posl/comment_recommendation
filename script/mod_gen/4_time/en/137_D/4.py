def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x:x[0])
    #print(jobs)
    total = 0
    for i in range(N):
        if jobs[i][0] <= M:
            total += jobs[i][1]
            M -= 1
        else:
            break
    print(total)

if __name__ == '__main__':
    main()