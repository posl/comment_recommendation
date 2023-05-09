def main():
    # Read input
    n = int(input())
    jobs = []
    for _ in range(n):
        a, b = map(int, input().split())
        jobs.append((b, a))
    jobs.sort()
    # Check if it is possible to complete all jobs
    time = 0
    for b, a in jobs:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")
