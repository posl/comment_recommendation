def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += jobs[i][0]
        if t > jobs[i][1]:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()