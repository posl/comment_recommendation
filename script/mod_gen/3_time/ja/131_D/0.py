def main():
    n = int(input())
    jobs = []
    for _ in range(n):
        a, b = map(int, input().split())
        jobs.append([a, b])
    jobs.sort(key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")
main()
