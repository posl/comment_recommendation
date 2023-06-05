def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[0])
    # print(jobs)
    # print(m)
    if m == 0:
        print(0)
        return
    ans = 0
    for a, b in jobs:
        if m >= a:
            ans += b
            m -= a
        else:
            ans += m
            break
    print(ans)

if __name__ == '__main__':
    main()