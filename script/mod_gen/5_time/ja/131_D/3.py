def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        jobs.append([A_i, B_i])
    jobs.sort(key=lambda x: x[1])
    t = 0
    for job in jobs:
        t += job[0]
        if t > job[1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()