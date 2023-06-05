def main():
    n, m = map(int, input().split())
    job = []
    for _ in range(n):
        job.append(list(map(int, input().split())))
    job.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if job[i][0] <= m:
            ans += job[i][1]
            m -= job[i][0]
        else:
            ans += job[i][1] * m
            break
    print(ans)

if __name__ == '__main__':
    main()