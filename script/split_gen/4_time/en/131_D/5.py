def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")
