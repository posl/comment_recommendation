def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append([B, A])
    jobs.sort()
    time = 0
    for i in range(N):
        time += jobs[i][1]
        if time > jobs[i][0]:
            print('No')
            return
    print('Yes')
