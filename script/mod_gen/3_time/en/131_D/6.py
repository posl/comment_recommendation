def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for i in range(N)]
    jobs.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()