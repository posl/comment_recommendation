def main():
    n = int(input())
    jobs = []
    for _ in range(n):
        a, b = map(int, input().split())
        jobs.append((b, a))
    jobs.sort()
    time = 0
    for b, a in jobs:
        if time + a > b:
            print('No')
            return
        time += a
    print('Yes')
