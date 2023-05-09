def main():
    N = int(input())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for B, A in jobs:
        time += A
        if time > B:
            print("No")
            return
    print("Yes")
