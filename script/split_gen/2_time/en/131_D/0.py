def main():
    N = int(input())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[1])
    now = 0
    for i in range(N):
        now += jobs[i][0]
        if now > jobs[i][1]:
            print('No')
            return
    print('Yes')
