def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x:x[0])
    result = 0
    i = 0
    while m > 0:
        if i == n:
            break
        if m >= jobs[i][0]:
            result += jobs[i][1]
            m -= jobs[i][0]
        else:
            break
        i += 1
    print(result)

if __name__ == '__main__':
    main()