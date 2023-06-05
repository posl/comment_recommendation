def main():
    n = int(input())
    jobs = [list(map(int, input().split())) for i in range(n)]
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()