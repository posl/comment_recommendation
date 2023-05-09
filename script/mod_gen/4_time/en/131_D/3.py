def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for job in jobs:
        time += job[1]
        if time > job[0]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()