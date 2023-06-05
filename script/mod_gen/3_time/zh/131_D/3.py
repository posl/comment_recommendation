def main():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()