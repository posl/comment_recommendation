def main():
    n = int(input())
    jobs = []
    for _ in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs = sorted(jobs, key=lambda x:x[1])
    time = 0
    for a, b in jobs:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()