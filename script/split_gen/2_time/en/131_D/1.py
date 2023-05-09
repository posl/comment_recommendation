def main():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((b, a))
    jobs.sort()
    time = 0
    for b, a in jobs:
        time += a
        if time > b:
            print('No')
            return
    print('Yes')
