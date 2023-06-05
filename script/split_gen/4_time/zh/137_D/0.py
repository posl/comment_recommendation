def main():
    n, m = map(int, input().split())
    job = []
    for i in range(n):
        job.append(tuple(map(int, input().split())))
    job.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if job[i][0] <= m:
            ans += job[i][1]
            m -= job[i][0]
        else:
            ans += job[i][1] * m
            m = 0
            break
    print(ans)
