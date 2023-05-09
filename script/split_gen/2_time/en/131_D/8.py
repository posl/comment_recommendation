def main():
    N = int(input())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for j in jobs:
        time += j[0]
        if time > j[1]:
            print('No')
            return
    print('Yes')
