def main():
    N = int(input())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x:x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")
    return
