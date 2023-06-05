def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if m > jobs[i][0]:
            ans += jobs[i][1]
            m -= 1
    print(ans)

if __name__ == '__main__':
    main()